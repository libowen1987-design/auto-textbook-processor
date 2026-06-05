# Kraus《Antennas》2nd Edition — Chapter 14
> **中英双语版**



## Chapter 14: Conformal Antennas



S56 APPENDIX A TABLES FOR REFERENCE APPENDIX



A-i0 BEAM WIDTH AND SIDELOBE LEVEL FOR



RECTANGULAR AND CIRCULAR APERTURE ,



_____ Aperture field distrntion ait power Level of ist



Rectangular or linear apertures El) beam width sidelobe, 4B CRO RAS



Tapered to S at edge(~10dB 7 cae -19 CODES



down) Els) = 1 2x°/3 tr), & ( )



Tapered to zero al edge Lom 1 +



Ex) = 1 — x? cos (x/2) ZN tL, i



Tapered to zero at edge Lue 32



E(x) = cos? (nx/2} WANG L,



Circotar apertures Bn) ‘



Uniform C—_) D, “" 1. Horizontal dipole arrays over imperfect ground. Computer programs for pat-



b—D,—+4 tern and gain calculations of HF horizontal dipole arrays over imperfect



. 66 ground were developed in 1986 by the International Radio Consultive Com-



Topered wo bet oan Cau Dy -3B mittee (CCIR). These programs in BASIC are available on disks from the



i) ort z International Telecommunication Union, General Secretariat (Sales Section),



° s Place de Nations, CH-1211 Geneva 20, Switzerland. The programs have the



Tapered to zero at edge ZN a -25 J code name HFMULSLW-HFDUASLW.



Bide tor 3 | 2. Three-d pattern plots. A computer program that plots antenna patterns in a



3-dimensional form (with hidden lines not plotted) was written in 1982 by



Tapered to zero at edge / \ bal 3 | W. A. Sandrin in FORTRAN IV. It is available as ASIS-NAPS Document



Ee) =(1—rP Ds : NAPS-04053 in photocopy or microfiche from NAPS c/o Microfiche Pub-



Tm UL Bw DL Wu umuned at b> 1 and D, > 1 Fora unio etnplr or Wea | lications, PO Box 3513, Grand Central Station, New York, NY 10163.



aperture MPBW = S1°/L, with first sidelobe — 13 dB, See also Tables 12-3 and 13-1. | 10163.



3, The Numerical/Electromagnetics Code (NEC).' This program or code has



| been under development for many years. It is a hybrid code which uses an



Electric Field Integral Equation (EFIE) to model wire-like objects and a Mag-



| netic Field Integral Equation (MFIE) to model surface-like objects with time-



1 "J. K, Breakall, G. }. Burke and E. X. Miller, “The Numerical/Electromagnetics Code,” Lawrence



| Livermore Natl. Lab., Document UCRL-90560, 1984.



BSS APPENDIX @ COMPUTER PROGRAMS (CODES)



Bz BASIC PHASED-ARRAY ANTENNA PATTERN PROGRAMS 859.



harmonic excitation. A 3-term sinusoidal spline basis is used for the wire witon,



current and a pulse basis for the surface current. Antennas and scatterers can i EEE “dns Prop Rao ca ne Gilsson, “Teangulir Patch Modkting of Arbitrary Bodies”



be modeled in their environments. Users of this program and also of almost all See ako y of Washington, 1979.



computer models should be aware of the uncertainty of solution accuracy and teferences at the end of Chap. 9.



validity. Therefore, are the number of wire segments or surface patches ade-



quate? Adding more can be ‘expensive and may actually be ambiguous if con- B2 BASIC PHASED-ARRAY ANTENNA PATTERN



vergence is not monotonic. . GRAMS.' These BASIC PRO-



‘an 8000-line program by G. J, Burke, A: J. Poggio and E. K. Miller of arrays of i programs supplement those of Chap. 4 for linear



: . . oe ys of isotropic sources of equat R .



available fc t a quat amplitude and sj .



Lawrence Livermore National Laboratory is avalable for ration or at based on (46-5) and (4-614), provide nermalized Rell and power pattere Ta



tering {rom a wire structure in free space or over @ ground P! lane (date 1980). polar and rectangular coordinates for a variety of conditi ane re tin ani in



4. Wire Antenna Program. A 5000-line FORTRAN IV program by R: J. Mar. end-fire, angle-fire and interferom ions including broadside,



pia of the ElectroScience Lab (OSU) is available from W. D. Burnside of the / phasing S (tad) and multiplying (or scale) fae for W sources with spacing D (1)



laboratory for radiation, gain and scattering of wire antennas near conducting soft BASIC. To change to IBM GW.BASIC soe MF. These programs are Apple-



structures. Incorporates NEC (date 1978). G see note on page 862.



5. Wire and Plate Program. A 4000-line FORTRAN program by F. H. Newman fencral program (field pattern, polar plot):



and D. M. Pozar of the ElectroScience Lab (OSU) is available from E. H. ° 10N = ?:D=?:S=?:MF=?



Newman for impedance, currents, radiation and scattering of 3-dimensional i 20 HOME: CD = 6.28*D



objects consisting of wires and/or plates. See E. H. Newman and D. M. Pozar, % 30 HGR



“Electromagnetic Modeling of Composite Wire and Surface Geometries,” 4 40 HCOLOR = 3



IEEE Trans. Ants. Prop. AP-26, November 1978. 50 FOR A = .01 TO 6.27 STEP 01



Other codes (programs) are listed at the end of Chap. 9. 60 CA = COS{A): PF = CD*CA +S



70 R = SIN(N*PF/2)/SIN(PF/2)



B-1 ADDITIONAL COMPUTER PROGRAM REFERENCES 90 HPLOT 138 + R*CA, 79 + R*SIN(A)



Baum, C, £.: “Emerging Technology for Transient and Broadband Analysis and Synthesis of > 100 NEXT A



Antennas and Scatterers,” Proc. IEEE, 64, November 1976 S i



Brittingham, J. N. E. &. Miller and J. L. Willows: * Pole Extraction from Real-Frequency Informa- q



tion,” Proc. IEEE, 68, 263-273, February 1980. Program 1. Broadside array of 4 sources with 4/2 ins, Fi i



urke,G. J, and E. K. Miller: “Modeling Antennas Near to and Penetrating Lossy Surface,” H | should read: /2 spacing, First or menu line



Lawrence Livermore Lab. Rept. 89838, 1983. } ON =4:



Burke, G, J, E. K. Miller, J N. Brittingham, D. L. Las R. 1. Lytle and 37. Okada “Computer i =4:D=.5:S =0: MF = 168



Modeling of Antennas near the Ground,” Electromag. 1, 29-49, 1981, Inchudes ¢<rent dis- Pr ‘



aieeeling od elevation patterns of Beverage antet®2S : Program 2. Ordinary end-fire array of 8 sources with 4/4 spacing. First line



Hartington, R. F.,and J. R. Mantz: “Theory of Characteristic Modes for Conducting Bodies,” IEEE i :



Trans. Ants, Prop., AP-19, 622-629, 1971 10N = 8:D = .25:S = — 1.57: MF = 84



McDonald, B.H,, and A. Wexler: “Finite-Element Solution of Unbounded Field Problems,” IEEE 3 . "



"Trans. Microwave Theory Tech, MTT-20, 841-847, December 1972. Program 3. End-fire array with increased-directivity of 8 sources with 4/4



Miller, E. K.; "Numerical Modeling Techniques,” Lawrence Livermore Lab. Rept. 89613, 983. spacing, First line should read:



Miller, E. K., G. J, Burke and E. S. Selden: “Accuracy Modeling Guidelines for Integral-Equation =8:D=.25:



Evaluation of Thin- Wire Structures,” IEEE Trans Ants. Prop. AP-19, 1971. 10 N = 8: D = .25:S = —1.96: MF = 13.1



Miller, E. K. and F. 3. Deadrick: “Some Computational Aspects of Thin-Wire Modeling,” in R. 1 Program 4. End-fire array with increased-directivi a a



Mittra (ed.), Numerical and Asymptotic ‘techniques ™ Ejectromagnetics, Springer-Verlag, 1975, q | spacing. First Sine should Tad. increased-directivity of 24 sources with 4/4



Miller, E. K., F. J. Deadrick and G. J. Burke: “Compute Graphics Applications in Electromagnetic 10 N = 24:D = .25:S = —1.70: MF = 4.38



Computer Madeling,” Electromag., 1, 135-153, 1981.



Rautio, J. C.: “Reflection Coefficient Analysis of the Effect of Ground on Antenna Patterns,” IEEE 1 Sone eas



“Ants, Prop. Soc. Newsletter, 29, 5-1, February 1997 j joe asitance of Marc Abel in preparing these Apple compatible programs is gratefully acknowt-



0 aveenon » counuren exocnans coD85 8:2 BASIC PHASED-ARRAY ANTENNA PATTERN PROGRAMS 861



L MF = 67/N. For increased directivity, however, all sources do not add in phase



Lo ; V4 at the pattern maximum so make MF = 67*SIN(1.57/N).



“sy g - : - - For power pattern, polar plot change line 80 to:



veel DAY AK 2 NLA XR LS 80 R = MFPABS(R)*ABS(RYIN



~ 1 2 ~ 3 4 For adding polar plot coordinate lines to programs ! through 8 continue



from line 80 as follows:



ATI, AS \ re rN panes 90 HPLOT 138 +R*.83*CA, 79+ R*SIN(A)



LK Loe fie Aad a a an 100 NEXT A



‘ nape : aN} & 110 FOR X = —58 TO 58 STEP 1



\ Ap XX PS OP RR Ly i 120Y =0



SETA as ae Nhe NEO 130 HPLOT 138 +X, 79+



* Le aa - 140 NEXT X



Figure B-t Polar field patterns for the 8 computer program examples of linear phased arrays of N 150 FOR Y = —67 TO 67STEP 1



isotropic sources along the horizontal axis. The 3-dimensional patterns are figuces-of-revolution 160X =0



around the horizontal axis. Ths, in the broadside patterns | and 8 the mainlobe is a disc and in the !



endefire patterns 2, 3 and 4 the main lobe is like a balloon or zeppelin. The main lobe in 5 is conical, H 170 HPLOT 138+X, 79+Y



as are the lobes between broadside and end-fire in 6 and 7. The inner circle is at half-power. 1s ner 50 TO 50 ST



Program 5. Angle-fire array (beam at 30° from broadside) of 16 sources with Afr 210 HPLOT 1384+X,79+Y



spacing, First line should read: 220 HPLOT 138-X, 799-Y



230 HPLOT 138+X, 79—



JON = 16: D =.5:8 = -1:57: MF = 42 MOHPLOT labo e soay



Program. 6. Interferometer 2-source array with 4A spacing. First line should , 250 NEXT X



read: j 260 FOR X = ~29 TO 29 STEP 1



10N = 2:D =4:S = 0: MF = 33.5 . 380 HPLOT 138 +X, 79+



Program 7. Broadside array of 8 sources with 24 spacing and grating lobes. 290 HPLOT 138-—X, 79—Y



First line should read: 300 HPLOT 138 +X, 799-Y



10N =8:D=2:S=0:MF =84 wONEXTX et



Program 8. Broadside array 12 sources with 4/2 spacing. First line should read: i 330 FOR A = 01 TO 6.27 STEP 0!



“ea. ‘ 340 HPLOT 138+ 56*COS(A), 79 +67*SIN(A)



10.N = 12:D =.5:8 =0: MF = 56 350 HPLOT 138 + 40*COS(A), 79 +47*SIN(A)



Polar field patterns for the above 8 programs are shown in Fig. B-1. 360 NEXT A



Compare the grating lobes of (7) with Fig. 11-78. RUN



For different numbers of sources (N), spacings (D) and phasings (S) an . . . _



unlimited variety of patterns are possible. Combinations of broadside and end- or ame) ering ine above 36-line progam and storing it on a disc, an infinity



fire arrays are left as an exercise. For example, a broadside array (as in Program 4 ‘th the ie ited in be calcula’ th ” iaole y simply entering a new line



1 but with D = 1.5) of 4 end-fire arrays (as in Program 3) results in a 32-source q! with the desired parameters as in the 8 example programs.



area array of high gain and small sidelobes in the plane of the array. | _ . .



« . . . The factor *.83 in line 90 equalizes the X and Y scales on the-printer used.



Although the magnification factor MF is arbitrary, the product of N and : Equivalent equalizing factors are written into the X and ¥ instructions for the



MF should be a constant for all pattern maxima to be equal (or normalized) coordinates. These factors may be modified itted.



when sources add in phase. Thus, in the above examples N*MF = 67 or 7 ¥ De modihed of omitted.



862. APPENDIX B COMPUTER PROGRAMS (CODES) APPENDIX



For field pattern, rectangular plot change lines 80 and 90 to:



For power pattern, rectangular plot change lines 80 and 90 to:



80 R = MF*ABS(R)*ABS(R)/N BOOKS



90 HPLOT A*30, 75—R AND



To run the above programs as IBM GW-BASIC programs: VIDEO TAPES



Change HGR to SCREEN 2. \



Change HPLOT to PSET with parentheses enclosing the rest of the line.



Abraham, M., and R. Becker: Electricity and Magnetism, Stechert, 1932.



Abaroni, J.: Antennae, Oxford, 1946.



Bahl, I.J., and P. Bhartia: Microstrip Antennas, Artech House, 1980.



Balanis, C. A.: Antenna Theory: Analysis and Design, Harper and Row, 1982.



Biraud, F. {ed.): Very Long Baseline Interferometry Techniques, Cepadues, 1983.



Blake, L. V. Antennas, Artech House, 1984.



Born, M.: Optik, Springer, 1933.



Bowman, J. J. T. B. A. Senior and P. L. E. Uslenghi: Electromagnetic and Acoustic Scattering by



Simple Shapes, North Holland. Amsterdam, 1969.



Bracewell, R.N.: The Fourier Transform and Its Applications, McGraw-Hill, 1963.



Bracewell, R.N.: The Hartiey Transform, Clarendon Press, Oxford, 1986.



Brillouin, L.: Wave Propagation in Periodic Structures, McGraw-Hill, 1946.



Brown, George H.: And Part of Which 1 Was, Angus Cupar (117 Hunt Drive, Princeton, NJ 08540),



Briickmann, H.: Antennen, ihre Theorie und Technik, Hirzel, 1939.



Burrows, M. L.: ELF Communications Antennas, Peregrinus, 1978.



Cady, W. M., M. B. Karelitz and L. A. Turner: Radar Scanners and Radomes, McGraw-Hill, 1948.



‘Christiansen, W. N., and J. A. Hogbom: Radio Telescopes, Cambridge, 1969, 1985,



Clarke, J. (ed.): Advances in Radar Techniques, Peregrinus, 1985.



Clarricoats, P. 5. B., and A. D. Olver: Corrugated Horns for Microwave Antennas, Peregrinus, 1984.



Collin, R. E.: Antennas and Radiowave Propagation, McGraw-Hill, 1985.



Collin, R. E., and F. J. Zucker (eds.): Antenna Theory, McGraw-Hill, 1969.



Cornbleet. S.: Microwave Optics: The Optics of Microwave Antenna Design, Academic Press, 1984.



Delogne, P.: Leaky Feeders and Subsurface Radio Communication, TEE, London, 1982.



Elliott. R. S.; Antenna Theory and Design, Prentice-Hal!, 1981



| Evans. J. V.. and T. Hagfors (eds.): Radar Astronomy, McGraw-Hill, 1968.



864 APPENDIX BOOKS AND VIDEO TAPES c2 vino tapes 865



Fanti, R, K. Kellermann and G. Setti {eds}: VLBI and Compact Radio Sources, Reidel, 1984. ' Rayleigh, Lord: The Theory of Sound, Macmillan, 1877, 1878, 1928, 1937.



Faraday, M.: Experimental Researches in Electricity, Quaritch, 1839, 1855. ; Reich, H. J. (ed.): Very High Frequency Techniques, McGraw-Hill, 1947.



Galejs, J: Antennas in Inhomogeneous Media, Pergamon, 1969 Reintjes, J. F. (ed.): Principtes of Radar, McGraw-Hill, 1946.



Hall, G. L. (ed): ARRL Antenna Book, American Radio Relay League, 1984. Rhodes, D. R.: Introduction to Monopulse, McGraw-Hill, 1959.



Hallén, E.: Teoretisk Electricitetslara, Skrivbycan Standard, 1945. Rhodes, D. R.: Synthesis of Planar Antenna Sources, Clarendon Press, Oxford, 1974



Hansen, R. C.: Microwave Scanning Antennas, vols. 1, 2, 3, Academic Press, 1966 Rudge, A. W., K. Milne, A. D. Olver and P. Knight (eds): Handbook of Antenna Design, Peregrinus,



Harper, A. E.: Rhombic Antenna Design, Van Nostcand, 1941 1983. ;



Hartingtor® R. F.: Field Computation by Moment Methods, Macmillan, 1968 Rumsey, V. H.: Frequency Independent Antennas, Academic Press, 1966.



Hertz, Heinrich, R.: Electric Waves, Macmillan, 1893: Dover, 1962. Rusch, W. V. T. and P. D. Potter: Analysis of Reflector Antennas, Academic Press, 1970,



Hertz, Heinrich: Memoirs, Letters, Diaries, San Francisco Press, 1977. Schollcmnoff, S. A.: Electromagnetic Waves, Van Nostrand, 1948,



Hoid, R. M.: Remote Sensing, Methods and Applications, Wiley, 1986. Schelkenotl,S. A.: Advanced Antenna Theory, Wiley, 1952. ,



Hudson, J. E: Adaptive Array Principles, Pereccinus, 1981 Schelkunoff, S. A, and H. T. Friis: Antennas: Theory and Practice, Wiley, 1952.



Huygens C. Prattede la Luminigre. Leyden, 1690 Sherman, S. M.: Monopulse Principles and Techniques, Artech House, 1984,



James, G. L.: Geometrical Theory of Diffraction for Electromagnetic Waves, Pecegrinus, 1980. Silver, S.: Microwave Antenna Theory and Design, McGraw-Hill, 1949.



James, J. R., P.S. Hall and C. Wood: Microstrip Antenna Theory and Design, Peregrinus, 1982 Sfoinik, “ ut puroduction to Radar Sytem. Mee on 1980,



Jame DM. and MC. devuchime C Son later, J. C.: Microwave Transmission, McGraw-Hill, 1942.



% fouse, 1983. feruchim: Communication Satellites in the Geostationary Orbit, Artech Slater, J. C., and N. H. Frank: Introduction to Theoretical Physics, MoGraw-Hill, 1933.



asi , Smith, C. E.: Directional Antennas, Cleveland Institute of Radio Electronics, 1946.



Johnson, R. C., and H. Jasik (eds,): Antenna Engineering Handbook, McGraw-Hill, 1984 ' ‘ ‘ .



Johnson, R. C., and H, Jasik (eds): Amenna Applications Reference Guide, McGraw-Hill, 1987, Smith, C. E.: Theory and Design of Directional Antenna Systems, National Association’ of Broad-



(Selected chapters from Antenna Engineering Handbook.) 4 s arene ples of A and Array 5 wi 6



Jordan, E, C, and K, G. Balmain: Electromagnetic Waves and Radiating Systems, Prentice-Hall, 1968. aera W. Land A v4 seen nn hee and Design, Wiley, 197



ull, E. Vi; Antennas and Diffraction Theory, Peregrinus, i981 Stutzman; W. L. and G. A. Thiele: Antenna Theory and Design, Wiley, 1981.



Kiely, D.G Disletrie Aerials, Methuen, 1953, Tai, C-T: Dyadic Green's Functions in Electromagnetic Theory, Intext, 1971.



King, R. W.P.: The Theory of Linear Antennas, Harvard, 1956. | Thommen A nat x tora one W Seeman tee hmerferometry and Synthesis in Radio



King, R. W. P., R. B. Mach . : of i *omomay, Wiley: . uo



ing, RW. Po RB. Mach and S. 8. Sanler: Arays of Cindi Dipole Antennas, Cambridge, “Astronomy, Wiley Interscience, 1986.



, . : Tseitlin, N. M.: Practical Methods of Radioastronomical and Antenna Techniques, Soviet Radio, 1966.



King. R. W. P, H.R. d ? oentai. .



in RY: Ba HER Mimo and AH. Wing: Transmission Lines, Antennas and Wave Guides. Uchida, H.: Fundamentals of Coupled Lines and Multiwire Antennas, Sasaki (Sendai), 1967.



King. WP. and G. 8 Smith: Antennas in Metter, MIT Press, 1990 Uda, Shintaro: On the Wireless Beam of Short Electric Waves. Series of 11 articles on his wave canal



Cee Di Eleciromagueien McGrane, 1958, 1973. 1988. (Yagi-Uda) antenna published in J. IEEE Japan, between March 1926 and July 1929, plus



Kenia) Des Radio Aehonons, Copia Quasar (PO Bor 3s, Powel, OH 43065), 1966, 1986, i ‘earlier and later articles on meter wavelength experiments. Privately published bound volume.



Keay De Bis Bon Coonan ueen isi } Powell, 1986. J Uda, §.: Short Wave Projector, Tohoku University, 1974.



Kuzmin, A. D., and A. 8. Solomonovich: Radio Astronomical Methods for the Measurement of Uda, S. and Y. Mushiake: Yagi-Uda Antenna Tohoku University, 954 i



ae Reena an Unaby, F.T., R.K. Moore and A. K. Fung: Microwave Remote Sensing, Actioe and Passive, Addison-



" 7 1974, : Wesley, 1985,



Landau, L., and E, Lifshitz: The Classical Theory of Fields, Addison-Wesley. 1951 Wait, J. R: Antennas and Propagation, Peregrinus, 1986.



Laport, E. A.: Radio Antenna Engineering, McGraw-Hill, 1952 : ?



Law, P. E., Jt.: Shipboard Antennas, Atech House, 1986. : Walter, CHL: Traveling W ave Antennas, Doven 1972.



Caan ae eee ec te oe ach House, 1986 Watson, W. H.: The Physical Principals of Wave Guide Transmission and Antenna Systems, Oxford,



A. 1, aad K. I 0 , . 1961.



Lo, Y.T. (ed.): Handbook of Antenna Theory and Design, Van. Nosirand Reinhold, 1987 Weeks, W. L.: Antenna Engineering, McGraw-Hill, 1968



Love, A. W.: Electromagnetic Horn Antennas, IEEE Press, 1976. Wood, P. 1: Reflector Antenna Analysis and Design, Peregrinus, 1980.



Love, A. W.: Reflector Antennas, IEEE Press, 1978, Wi iil, 19) :



; - neck, J: Wi -Hill, 1915.



Luneburg, R. K.: Mathematical Theory af Optics, Brown University Press, 1944 Zen ielefs Telegraphy, McGraw-Hil, 1915



Ma, M..: Theory and Application of Antenna Arrays, Wiley, 1974



Mar, J. W., and H. Liebowitz (eds): Structures Technology for Large Radar and Radio Telescope C2 VIDEO TAPES



‘Systems, MIT, 1969. Kraus, J. D.: “Antennas and Radiation,” Lecture-demonstration, excellent teaching supplement, 70



Marconi, Degna: My Father Marconi, McGraw-Hill, 1962 min. color, VHS. Cygnus-Quasar, P.O. Box 85, Powell, OH 43065.



Marcuse, D.: Theory of Dielectric Optical Waveguides, Academic Press, 1974. Landt, J. A., and £. K. Miller: “Computer Graphics of Transient Radiation and Scattering Pheno-



Maxwell, J. C.: A Treatise on Electricity and Magnetism, Oxford, 1873. ‘mena on Antennas and Wire Structures,” Fields and currents in slow motion, 15 min, color,



Monzingo, R. A., and T. W. Miller: Introduction to Adaptive Arrays, Wiley, \980. ‘VHS. Cygnus-Quasar, P.O. Box 85, Powell, OH 43065.



Mouilin, E. B.: Radio Aerials, Oxford, 1949.



Poincaré, H.: Theorie Mathematique de la Luminiere, Carte, 1892. . 1



Popovic, B. D., M. B. Dragovic and A. R. Djordjevic: Analysis and Synthesis of Wire Antennas, Wiley. :



Pozar, D.: Antenna Design Using Personal Computers, Artech House, 1985. i



APPENDIX ANSWERS TO STARRED FRosLems 867



(@) Max. at 0°, 180°, 441.8", S138.2"



Nulls at +194", +90", £1606"



Half-power at +9.6°, £1704", +30, S150", +56.5°, +123.5°



OO (e) Max. at 0°, 180", + 14.5%, +165.5°, £30", + 150%, +49", + 131°, 490°



Nulls at £7°, +173°, +22", S158, +39%, S141", 461°, £119°



ANSW Half-power at £36", +£1765', S11", £169", £185", £1615", £26, +154° S34.5",



ERS TO £145,5°, £435", £1365", £545, S125.5, +70", £110"



STARRED (Jf) Max. at 0°, 180°



44, — {sin Gin sin #) (15



{0) 1g) = cos? (jx sin g) of 3 cos (Gx sin g) + 3.005 (ga sin 4)



446 (a) 0.52, 0.82, 1.00, 0.82, 0.52



{b) Max. at +39°, + 141°, + 90°



Nulis at +30", 454°, +126, +150"



415, R = S:0.93, 0.84, 1.00, 1.00, 0.84, 0.93



R = 7: 0.69, 0.80, 1.00, 1.00, 0.80, 0.69



R = 10; 0.53, 0.78, 1.00, 1.00, 0.78, 0.53



CHA! 418 (0) = SEE were y= d cos d+ 6



24, 116i 422. (a) and (b) 1 major and 5 minot lobes, (c) ordinary D ~ 7; ine, dir.: D ~ 12



29, 152m? RCP 4-25, (6) 6.6, (c) 6.3



2k. (a) AR = 1.5, (b) r= 90°, (c)} CW 434. 0.61



213, (6) AR = 1.38, (c) = 45° 4-38. Max. 0°, 180°, +60°, +90", +120"



2-15, Straight line with t = 45° Min. +41.4°, +75.5°, + 104.5, S138.6



218, (a) AR = 2.33 (RH), (6) r= — 45°, (c) RH 4-44, (a) 44°, (b) —13.3 AB, (0) 0.17 sr, (4) 0.89, (€) 24,(f) 1.927



2-20. (a) AR = —5,(b) RH, (c) 34 mW m=?



2-22, (a) AR = 3.0, (b) = —22.5°, (c) CW, (@) LH



BA. (a) 5.1, 6; 7.07; (6) 3.8, 4.6, 6.1 Qt cos 8 Qisin®



33. (a) 1539 W m™?, (b) 4.29 x 1076 W, (c) 762 V m7! SA. 0) B= Sr Be ane En



S3. (@) E= tan O sin G cos °) (by 168 , (c} 168, 73, 1970



41. (c) Max. at 0", +90", 180° S6 (@) B= p cob ale ¢ —cos } 4-lobed patterns



Nulls at + 30°, +150°



Half-power at +14.5°, +1655°, +486", +131.4° 7 o soiobed pattern



S13, (a) 8.16, (6653.0



- 68 aprENDIXD ANSWERS TO STARRED PROBLEMS 869



CHAPTER 6 CHAPTER 13



62, 4lobed pattern 131 7109



CHAPTER 7 163. (a) 625 mm,(c) 28%



Tet. (10.802, (2) 0.763



J2Hi,jn, (0) E = sin 8



1-6, (a) Dy afm, (0) CHAPTER 16



CHAPTER 8 16-6, (a) 26.5 W m~?, (b) 184 «W m=?



1043500 16-8 5.35nWm-?



83 2704) 16-11. f, = 0,8.89/4) Np m=!



16-14. See App. E and Fig. E-1



16-17. (a) 5°, 1 dB; 10°, 22 4B



CHAPTER 10 (0) 5°, L4 dB; 10°, 29 4B



jou. 121 +5460 (c) 5°, 0.06 @B; 10°, 0.26 dB



105. R= 500,R,=.200,R, = 500 16-21, 106, 35, 11 and 3.5m



CHAPTER 11 (7-1, (a) 12.2 dB, (0) 23 m



Ld, (b) +0674 17-2, 145K



IL-7, (a).1 and 6: 63 + j29; 2 and 5: 46 ~ j2;3and 4: 53 + jl00 17-4. (a) 0.08 K,, (6) 0.09 K, (c) 445 K, (d) 500 mJy



HLA, (a) 52 — j210; (b) G, (max) = 1.55 17-8, (a) 0.06 K, (6) 320 mly



14-17, (6) ~17° 178 236K



11-98. 11.7° 17-18. (a) 127 dB, (6) 0.5 dB, (c) ~ 13 min



11-22, (a) 0.3544, (6) —/2 17-16, 65.1 kW Hz"!



16-26. H, = 083, 6 = 725% by = 55 17-18. (a) 15.6 MHz, (6) 26.4 MHz, (c) 41.0 MHz



MA2B, g = 72.5°, Ly = 5.14



11-34, (a) 6°22’, (by — 13.15 dB, (c) w/4 sr, (d) 0.89, fe) 16, (1) 127 CHAPTER 18



11-40, S 18-1, (a) 4.60 m, 21.2 m; (6) 25.2 mm, 116 mm; {c) 650 xm, 3.00 mm



CHAPTER 12 18-7. (a) 377.2, (0) 275 mm



126 (1) 73,0 1048 120-9908



124, () 164Bi 126 18-12. 57%



12-13, 76.6 m 19:13 ~34



1217, 81.1%, 1304 or 31.2 dBi



APPENDIX PROBLEM SUPPLEMENT 871



height, while with the HP and VP antennas the level varies from 6 dB more to no signal at



Another important (actor for TV reception is that with CP antennas the signal is



received (ideally) over only the direct path while with the HP and VP antennas the signa} is



Teceived via both direct and reflected paths. At maximum, the direct and reflected path



signals are essentially equal in level but arrive at different times. If the time difference is of



PROBLEM the order of a microsecond, objectionable ghost images will occur, degrading the picture



1614 (0) Note that the level with the CP antennas isthe same as would be obtained with either the



VP or HP antennas if the signal was received by the direct path only (no ground



reflection). However, with CP antennas the signal level is essentially independent of the



i | Horizontally polarized (HP)



5 50) ) Vertically polarized (VP}



af} circtarty polarized (CPI



Figure E-1 Solution to part (a) of Prob. 16-14 showing variation of vertical, horizontal and circular d



polarization signals with height above ground.



Abel, Mare, 8598, Bach, H., 619



| Abraham, M.. 43n, 359, 863 Bagby, C. K., 292



i Abramowitz, M., 252n Bahl, 1. J., 863



4 Adams, A. A., 3330 Bailey, Beetle, 723



Adams, N. I., 380n Baird, R. C., 8280, 830, 8310



Adatia, N. A., 621 Baker, D. E., 64n, 278n, 287n, S93, S94, 693, 842



Abaroni, J., 863 Balanis, C. A., 408, 863



Ajioka, T. S., 688n Balmain, K. G., 864



Akabane, K.. 609 Barkofsky. E. C., 79n, 767n, 827n



Alanen, E.. S36, 722n Barrow, W. L., 648n, 654n, 674n



Albert, G. E., 360n Barton, P., 536



Alford. Andrew, 79n, 230n, 251n, 630, 642n, Baum, C. E., 858



643, 692n, 732n, 7670, Bawer, R., 698n



Allen, 3. L., S36 Bechmann, R., 4130



Ampére, André M., 2 Beck, A. C., 503n, 505



Andersen, J.B, 2051 Becker, R., 863



Anderson, A. P., 619, 620 Bell, Alexander G., 5



Ando, M., 659 Bennet, J.C. 619



Andre, S.N., 496n Bennett, F. D., 7410



Andreasen, M. G., 408 Bernsten, D. G., 2778



Angelakos, D. J., 2870 Beverage, H. H., 508



Armitage, J. L., 715, Bhartia, P., 863



‘Armstrong, Major Edwin HL, 7 Bickmore, R. W., 499



Arvas, E., 797 Bingham, Linda, 4000



Ashenasy, J..748n Biraud, F., 863



Ashmead, J., S45n, 598 Blake, L. V., 863



Atia, A. E., 703 Blank, S., 499



nafler a page number signifies foomote. Boerner, W. M., 798



874 NAME INDEX NAME INDEX. 875



Bolomey. J. C.. 842 Cleckner, D.C. 480 Elkamchouchi, H. M., 560 Hall, G. L., 864



Booker, H. G.. 628, 630n. 634, 638,517 Clemmow, P. C.. 517 Ethiott, R. S., 408, 863 Hall, K., xxiv



Born, Max. (79n, 632n, 863 : Clerici, G. C., S91n, 619n, 819, 820, 821n Emerson, W. H.. 815 Halt, P. S., SOta, 864



Bose, Jagadis C.. 5. 15, 644 Cohn, S. B.. 6540 England, R. W., 6580 Hall, R. C., 798



Botha, L.. 64n Coteman. P. D., 7410 Enoch. J. M., 7168, Hallén, E., 360n, 3650, 368n, 372n, 374n, 864



Bowman, J. J., 798, 863 Collin, R. E., 863 Epstein, J., 7230, 7280 Hansell, C. W., 5020



Bracewell, R. N.. xxv. 517n, 521n, S22n, 528, Collington, G., 842 Erickson, N. R.. 645n Hansen, R. C., 488n, 499, S00, 713n, 798, 864



533, 577n, S78, 585, 863 Conti, R.. 495 Ersoy, O., 500 Hansen, W. W., 1420



Braun, F., 7330 Cornbleet, S., 863 Eshleman, ¥. R., xxiv, 690 Haslen, F., 843



Breakall, J. K., 8570 Cotton, R. B., 3280 Evans, J. V., 798, 863 Harper, A. E., 503n, 504, 864



Brillouin, L., 314n, 863 Coulomb, Charles A. de, 2 Harrington, R. F., 389,797, 858, 864



Brittingham, J. N., 858 Cowan, John D., Jr.. S7 Fati, H., 500 Harrison, C. W., Jr., 361n, 368n, 370n, 425n



Brookner, E., 7480 Cox, C. R., 4508 Fanti, R., 864 Hatcher, B. R., S00



Broussaud, G., 324n Crawford, A. B., 620 | Faraday, M., 2, 15. 864 Heideman, M. T., 500



Brown, G. H., 15, 132n, 3379, 354n, 372n, 421n, Cross, D. C., 620 Feldman, C. B., 5070 Heisler, R., S00



425n, 426n, 439n, 449n, 451n, 452, 453,454, Cutler, C. C., S64n, 810n, 824n, 827n | Felsenheld, G. A., 7230 Hendriksson, J., 496



473, 474, 479, 482, 503n, 545n, 7230, 727, Felsenheld, R. A., 7320 Henry, Joseph, 2



728n, 733n, 840n, 863 Dalle Mees, E., 798 Fenn, A. J., 536 Hertz, Heinrich R., frontispiece, xxiii, 1, 3, 16,



Bruce, E., 505 Davidovitz, M., 798 | Fligge, S., S170 864



Brdckmann, H., 509n, 863 Davis, J. H., 620 Fomichev, K. L., 864 Hertz, Johanna, 16



Burgener, R. W... 842 Davis, R.. xxiv qi Foster, Donald, 245n, 250n, 254, 503n Hewish, A., 535n



Burke, B. F., S35n Day, P.C., 331m Fouty, R. A., 7330 Hogbom, J. A., 587n, 863



Burke, G. J., 397n, 408, 857n, 858 De Vito, G., 706 Franceschetti, G., 59a Hogg, D. C., 620



Burnside, W. D., xxiv, 591n, 619, 620, 659, 693, Deadrick, F. J., 858 Frank, N. H., S69n, 865 Holland, J., 328n



799, 816, B18n, 819, 820, 821n, 822n, 842 Debye, P..-685n i Franklin, Benjamin, 2 Hollis, J.S., 809n



Burrows, C. R.. 7380 Delogne, P., 863 Friis, H. T., 48, 3980, 5070, 564n, 682n, 865 Hondros, D., 685



Burrows, M. L.. 863 Detneryd, A., 748 Fang, A. K., 798, 865 Hord, R. M., 864



Burrus, C. S., 500 Deschamps, G. A.. 75n, 696n, 703, 798 Horton, C. W., 6870



Butler, J. L.. 488n, 499 Dewitt, B.T.. 816, 8180 Gabriel, W. F., 536 Howard, 7». D., 620



Butson, P. C., 706 Dianat, S. A., 798 Galejs, J., 864 Howell, J. M., 536



Bystrom, A:, Jr., 277n Dinger, R. J., 499 Gauss, Karl F., 2 Hudson, J. E., 536, 864



Dixon, R. S., xxiv , Gerst, C. W., 3330 Huebner, D. A., 50Ln



Cady, W. M., 863 Djordjevic, A. R., 864 Geyer, H. 659 Hunt, L. B., 620



Cantoni, A., 798 Dolph, C. L., 161n Gilbert, William, 2 Huygens, C., 179n, 864



Carrel, R. L., 706, 707 Donn, C., 287n Gill, G. J., 6631, 690



Carson, J. R., 4100 Dore, A.. 353n, 372n, 374n, 3770, S93n, 545n, Gillespie, E. S., 830n, 842 Jams, Harley, 8241



Carter, P. S., 413n, 428n, 429n, 429n, 460n, 502n _627n, 630, 648n, 653n, 725n Gitreath, M. C., 591n, 619, 8190 Iguchi, M., 537



Carver, K. R., 277n, 278, 494n, 748 Dowling, T.. 495 Glasser, O. J., 266n Inagaki, N., 560



Chatterjee, J. S., 331n, 701 Doxsey, R., 535m Glinski, G., 245n Isbell, D. E., 703, 704



Chen. C. A., 4820 Dragone, C., 620, 659 q Glisson, A. W., 859 Ishigro, M., 609n



Chen, T-S, 654n Dragovic, M. B., 864 1 Godwin, M. P., 620 Ishimaru, A., S99, 620



Cheng, D. K., 190n, 4820 DuHamel, R. H., 338n, 703 Goldsmith, P. F., 615n, 663n, 690



‘Cheong, W. M., 706 Dunlap, Orrin E., 15 Gordon, W. E., 801 Jackson, J. D., 2940



Chin, 8. K., 500 Dybdal, R. B., 619 Gato, N., 659 James, G. L., 620, 864



Chireix, H., 510n Dyson, J. D., 696n, 697, 698n, 699, 702, 703 Gray, D. A., 605n, 658n James, J. R., 864



Christ; 1,1 Greenough, R. K., 3330 Jamieson, H. W., 2410



Christiansen, W. N., 587n, 863 Ecker, H. A., 809n, 819m Gregory, James, 596n Jamwal, K. K. S., 2870



Chu, L. J., 294n, 380n, 648n, 654n, 674n Enimiu, C,, 798 Griffiths, L. J., 500 Jansen, J. 1, 6540



Chu, T-S, 605n, 609, 619, 658 Ehrenspeck, H. W., 620 3 Grosskopf, J., 230n Jansky, D. M., 766, 864



‘Chuang, C. W., 620, 659, 693, 798 Einarsson, ., 499 ‘Gundlach, Friedrich W.. 15 Jansky, Kari G.. 7



Clark, H.K., 8270 Einstein, A., 689, 768 ‘Gupta, L J., 500 Jasik, H., 500, 864



Clarke, A. C., θ, 762 Ekers, R. D., 5340 Jaumann, J., 815, 842



Clarke, J., 798, 863 E-Masry, E. [., 500 Hacker, P.S., 810 Jenkins, W. K., S00



Clarricoats, P. J. B., 659, 863 ElectroScienice Lab, 858 Hagfors, T., 79% 863 Jeruchim, M. C., 766, 864



Mattes, H., 659 Newell, A. C., 828n, 830



Jim, C. Wo, 500 Lager, D. L. 858 Maute, JR. 797 Newman, E, H., xxiv, 397, 408, 798, 858



Johansson, J. J. 660  Lagrone, A-H.. 659 Maxwell, J. C.,2, 16, 864 Newton, Isaac, 3, 16



Johnson, H. W., S00 Lamb, J. W., 620 Mayer. £620 Nonier, JR. 842°



Johnson, R. C.. 328n, 809n, 819n, 842, 864 Landau, L., 52n, 864 Mayer @ HL 70 Nyguist, H., 770



Jordan, E. C.. 4, 642n, 696n, 864 Landsdorfer, F. M., 484 Maree Esai, 6960, 698n, 703, 707



Jordan, J. F., 5350 Landt, J. &., 865 McCullough, T. P., 7770 Oersted, Hans C., 2



Jul, E, V.. 864 Laport, E. A., 864 McDonald, B. H., 858 Ohm, Georg S., 2



Law, PE. Jr, 864 McGahan, R. V., 799 Okada, J. T., 858



Kajfu, N.. 609n Lawrence Livermore National Laboratory, 858 eee gis Olmen HG. 90in



Kajlez, D., 287n Lawson, J. D., 537 McNamara, D. A., 640 Olver, A. D., 659, 863, 865



Kandoian, A. G., 251m, 723n, 732n Laxpati, 8. R., 500 Medgyesi-Mitschang, L. N., 798, 799 Ott, R. H., 599, 620



Kaplan, P. D.. 620 Lazarus, D., 627n, 630 Mei, K. K., 408, 703 Owens, M., 750n



Kardashev, N., 8110 Legg, W. E., 605n, 658n i Meier, A. S., 741n, 833



Karelitz, M. B., 863 Leonard, D. 5.. 496a q Meier, P. J., 655. Pacht, E., xxiv



Kawakami, H., 7349 Leonov, A. 1. 864 | Mendelovicz, A., 3330 Page, L.. 380n



Kay, A. F., 657n, 659 Levine, E., 748n Mentzer, C. A., 660 Papas, C. H., 591.



Kelleher, K. S., S00, 689 Lewis, F. D., 648n Michael, Y., 842 Pathak, P. H., 620, 621, 798



Keller, 4. B., 620, 798 Lewis, Robert, 723n Mie, G.. 794 Patton, W. T., 328n, 332n, 3380



Kellermann, K. 1.,,5350, 864 Lewis, W. D., 564n, 682n Mikawa, T., 3310, 702 Payne, W., 621



Kellogg, E. W., 508 Liang, M. C. 822n Miller, E. K., 397n, 858, 865 Peace, G. M., 655



Kennaugh, E. M., 57, 408, 798 Lichowitz, H.. 864 Miller, T W., 864 Pelton, E. L., 604, 605



Kent, B. M., 591n, 619, 819" Lifshitz, E.. 52u, 864 Miller, W. E., 642n Penzias, A. A., 8, S99, 780, 842



Kerr, J. L., 693 Lindel, JV. L-, 536, 7220 Milligan, T. A., 6520 Peters, L., J, xxiv, 277n, 603, 620, 660, 799



## 中文翻译

> **中文：** 第14章介绍**共形天线(Conformal Antennas)**。共形天线是贴合于安装表面形状的天线，通常安装在飞行器、导弹、卫星或车辆蒙皮上，不产生空气动力学阻力。

### 14-1 共形天线概念
共形天线与安装表面形状一致，可以是圆柱形、球形、锥形或任意曲面形状。与平面天线相比：
- 不破坏载体的气动外形
- 节省空间
- 可覆盖更大空域

### 14-2 共形天线类型
- **共形微带天线阵**：在曲面上布置微带贴片单元
- **共形缝隙天线**：在导电蒙皮上开槽
- **共形螺旋天线**：用于宽带圆极化

### 14-3 关键设计挑战
- 曲面上的单元方向图畸变
- 单元间相互耦合分析复杂
- 馈电网络设计困难
- 制造工艺要求高

### 14-4 应用
机载雷达（包括机头共形阵）、导弹导引头、卫星通信、智能蒙皮、隐身平台天线系统。

# Kraus《Antennas》2nd Edition — Chapter 8
> **中英双语版**



## Chapter 8: Slot Antennas



430 10 SELF AND MUTUAL IMPEDANCES 104 MUTUAL IMPEDANCE OF OTHER CONFIGURATIONS 431



Table 10-2 Mutual resistance as a function of d and h (Fig. 10-15)



| for thin 7/2 antennas in echelon



| Spacing ¢ 00% Osi 10k MSA 20K SKA



q 004 473R1 42640-41418) 10 +06 04



O54 -127 -118 08 +08 -10 +05 -03



a-—- j 104 +438 S88 436-29 +11 -04 = +01



h 1Sk -24  --S8 «=--63 #20 +06 10 +09



; 204 +Ll S38 +63 4020-26 S160 05



25k -O8  -28 9-57-24 +27 -030 -O1



Figure (0-15 Two parallel linear 2/2 antennas in echelon 35% 03-15-39 38407) 4270-10



401. 402 +11 431 +37 405  -25  -03



454 -02 -09 -25 -34 -13 +20 +11



10-8 MUTUAL IMPEDANCE OF OTHER CONFIGURATIONS. so: 402 407 4210 43a 4184619



There are many other antenna configurations for which the mutual impedance 55h. -01 -06 -18 -29 -22 +405 +18



may be of interest. The variety is enormous, but two will be mentioned and 60% +01 +05 +16 426 423 -O1 -20



references given which the reader may consult for further information. 654 -O1 9-05) =12 =2300 -230 05 417



704 401 404 411 +21 423 409-13



1. Parallel antennas of unequal height. This case has been treated by Cox.' His TSA 00 -03  -10 -19 -24 -10 +07



data apply specifically to stub antennas perpendicular to an infinite, perfectly TTT —



conducting ground, but can be used with symmetrical center-fed antennas of Magnitude Orientation Periodic function



twice the length by multiplying the resistance and reactance values by 2 (see 60nL, L



also Howard E. King?). or Zy = rb Ld (in 9 sin 6°) (sin 2nr, + j cos 2nr,) (2)



2. V or skew antennas. Some antenna systems involve nonparallel finear radi- ra



ators. The mutual impedance of such inclined antennas are readily calculated i i i



° with maximum value



by the moment method, as, for example, by J. H. Richmond’s FORTRAN IV 60nL, Li



program, ASIS-NAPS Document NAPS-02223 (see References at the end of Z2,(max) = +) (3)



. . We note in (2) that there are 3 factors: the first is a magnitude factor involv-



For two short dipoles, however, a simple, useful relation can be derived as ing the lengths of the dipoles and their separation, the second involves their



follows. . . - mutual orientation, while the third factor is a periodic or complex function of unit



Referring to Fig. 10-16, consider the 2 short center-fed dipoles 1 and 2 of magnitude giving the phase as a function of the separation distance. The mutual



length L, and Ly separated bya distance n with orientation angles 6 and 6’ as impedance for antennas, in general, involves these 3 factors.



indicated. The mutual impedance Z,, is given by the ratio of the voltage V,,



induced in dipole 2 by the current [, flowing in dipole 1. Then for L, € 1, L; <1



and r, > 1, we have, from (5-2-34), e



Zu = t= —— sin 6 ee L, sin & (1) L,



1C. R. Cox, “Mutual Impedance between Vertical Antennas of Unequal Heights.” Proc. IRE, 35, Ly Figure 10-16 Two short center-fed dipoles of length L, and



1367-1370, November 1947. Li, with separation r, and orientation angles θ and 6 fot



? HE. King, “Mutual Impedance of Unequal Length Antennas in Echelon.” IEEE Trans. Ants. mutual impedance equation.



Prop., AP-5, 306-313, July £957.



432 10 SELF AND MUTUAL IMPEDANCES proptems 433



10-9 MUTUAL IMPEDANCE IN TERMS OF DIRECTIVITY separation distance is large compared to the antenna dimensions and also that



AND RADIATION RESISTANCE. Consider a transmitting antenna and rd A.



receiving antenna separated by a distance r. The power delivered to the receiv-



ing antenna load under matched conditions is Example. Calculate the maximum mutual impedance of 2 center-fed dipole



antennas 0,14 long separated by 104. Assume uniform current distribution on the



p= (4/2? wm w dipoles. The receiving antenna is terminated for maximum power transfer



where ¥, = voltage induced at terminals of receiving antenna, V Solution. From (6) and (2-20-3) (and also the table of Sec. 2-24),



R, = radiation resistance of receiving antenna, 2 4 1.5 x 0.8n?



(Zp [(max) = —S————— = 0.1885 2



The power transmitted is given by ™



P.=2R, (Ww) Q rom 10-83,



where /, = current at terminals of transmitting antenna, A Z3,(max) = — > 0.1885 0



R, = radiation resistance of transmitting antenna, Q ;



; Although (6) and (10-8-3) bear little resemblance, except for the r, in the denomina-



From (1) and (2), the magnitude of the mutual impedance of the antennas is tor, both yield an identical impedance.



Meai= fn MER wa EVER 8)



_ ADDITIONAL REFERENCES FOR CHAP. 10



From the Friis transmission formula (2-25-5),



Rhodes, D. R.: “A Reactance Theorem,” Proc, Roy. Soc: Lond, A, 383, \-10, 1977.



P, Aw An Uda, S., and Y. Mushiake: “On the Theory of Antennae with Discontinuous Thickness,” Tech. Rept.



Pre 4) Tohukst Unit:, 14, no. 2, 1950.



' Uda, S, and Y. Mushiake: “Theoretical Calculation of the Input Impedances of Two Parallel



where A,, ~ effective aperture or receiving antenna, m? Antennae,” Sci. Rept. Res. inst. Tohoku Unic., Bel, 2, no. 1, 1951.



A,, = effective aperture of transmitting antenna, m? ]



Introducing (4) in (3), the maximum mutual impedance becomes



BAD in GO Pe PROBLEMS!



_ 2S Ae Aa RR, 5 410-1 A Si/2 antenna. Caiculate the seif-resistance and self-reactance of a thin, sym-



Z,{max) = rh (5) metrical center-fed linear antenna Si/2 long.



10-2 Parallel side-by-side 4/2 antennas. Calculate the mutual resistance and mutual



However, the directivity D = 41A,/2?, so the maximum mutual impedance can be reactance for two parallel side-by-side thin linear 4/2 antennas with a separation



reexpressed as of 0.152,



/D,D.R_R, 10-3 Two 2/2 antennas in echelon. Calculate the mutual resistance and reactance of two



1Z,,|(max) = ——t  () (6) parallel thin linear 2/2 antennas in echelon for the case where d = 0.254 and



h = 1.252 (see Fig. 10-15).



where D, = directivity of receiving antenna, dimensionless 10-4 Brown’s equation. Prove Brown's relation Ry, — R21 = 60n°(d/i)? given in



D, = directivity of transmitting antenna, dimensionless (10-5-9).



R, = radiation resistance of receiving antenna, Q *10-5 Three side-by-side antennas. Three antennas are arranged as shown in. Fig. P10-5.



R, = radiation resistance of transmitting antenna, Q The currents are of the same magnitude in, all antennas. The currents are in phase



¥, = separation, wavelengths in (a) and (c), but the current in (6) is in antiphase. The self-resistatice of each



Thus, the mutual impedance of two antennas is a function of their directivities (or oT



apertures) and radiation resistances. In the above, the restriction applies that the * Answers to starred (+) problems are given in App. D.



434-0. SELF AND MUTUAL IMPEDANCES a



antenna is 100.2, while the mutual resistances are: Ry = Ry. = 40.2 and R,, = CHAPTER



10 © What is the radiation resistance of each of the antennas? The resistances



are referred to the terminals, which are in the same location in all antennas. Y l l



b ¢ Figure P10-5 Three side-by-side antennas. DIPOLES



10-6 Self-resistance and mutual resistance. Explain why the mutual resistance of two AND OF



antennas can be both positive and negative but the self-resistance of a single



antenna can only be positive. 8 eh APERTURES



10-7 Terminal impedance.



(a) Show by means of an equivalent network that at the terminals of a receiving



antenna, the equivalent, or Thévenin, generator has an impedance Z,,



(Z2/Z,,) and an emf ViZ_/Z,,. where Z,, = self-impedance of transmitting



antenna, Z)) = sell-impedance of receiving antenna, Z, = mutual impedance oi



and V, = emf applied to terminals of transmitting antenna.



(o) What load impedance connected to the terminals of the receiving antenna



results in the maximum power transfer?



; 11-1 INTRODUCTION. Essential background for this chapter is covered



i in Chap. 4 on arrays of point sources, Chap. 5 on linear antennas, Chap. Ton



4 driven element arrays (Secs. 7-11 and 7-12) and Chap. 10 on self and mutual



fl impedances. The heading for this chapter could appropriately be “Arrays of



° Antenna Elements” where an element refers to the basic unit of which an array is



constructed. In the first part of this chapter the “elements”. are mostly thin linear



dipoles while in the latter sections of the chapter the array “elements” are aper-



tures in general, which may be helices, horns, big redectors or arrays of dipoles



i (arrays of arrays).



The far- ot radiation field pattern, the driving point impedance and the array



| gain are first derived in that order for several different arrays of dipoles. The



4 method of analysis is general and is applicable to other dipole arrays, the specific



types discussed serving merely as examples. Array gain is calculated by treating



| the dipoles as circuit elements having self and mutual impedances. Although



direct pattern integration could be used to determine the gain, the circuit



approach is simpler provided impedance values are available (patterns having



| been utilized in the impedance calculations). In most of the arrays the dipoles are



driven but Sec. 11-9 discusses arrays having parasitic dipoles.



Retro, ohased, scanning, adaptive, microstrip, low-s'delobe, tong-wire and



curtain arrays are topics of Secs. 11-10 through 11-16. The remaining sections



436 11 ARRAYS OF DIPOLES AND OF APERTURES 12 ARRAY OF TWO DRIVEN i:2 ELEMENTS. BROADSIDE CASE 437



1 2 Figure 11-1 Broadside array of 2 in-phase 1/2 elements, i z



discuss continuous apertures, Fourier transform relations between far-field pat- - d 5 .



terns and aperture distributions, total power and correlation arrays, interferome-



ters, aperture synthesis, very large arrays and very long baseline arrays. a



11-2, ARRAY OF TWO DRIVEN 1/2 ELEMENTS. BROADSIDE x Q



CASE. Consider two center-fed 4/2 elements (dipoles) arranged side by side with 2 elements Eie) 2 elements) | £10)



spacing d as in Fig. 11-1. Two special cases will be considered: the broadside



case’ treated in this section, in which the two elements are fed with equal in-phase ~ 5 - 5



currents, and the end-fire case? (Sec. 11-3), in which the two elements are fed with



equal currents in opposite phase. The more general case Where the currents are rN ©



equal in magnitude but in any phase relation is treated in Sec. 11-4. | %



Figure 11-2 Patterns for broadside array of 2 tinear in-phase 4/2 elements with spacing d = 4/2.



11-2a Field Patterns. The first part of the analysis will be to determine the q | . . . ‘oh @ = 90° or xy plane in



absolute far-field patterns. It is convenient to obtain two pattern expressions, one and at a large distance D (D > d) in a horizontal plane (@ = 90° or xy pl



for the horizontal plane and one for the vertical plane. Ordinarily, the relative | Fig. 11-2a) is



patterns would be sufficient. However, the absolute patterns will be needed in re)



gain calculations. Let the elements be vertical as shown in Fig. 11-2a. It is E,(@) = ki,



assumed that the array is in free space, ie, at an infinite distance from the ground ; “yea . D and J, is the terminal



or other objects. The field intensity E,() from a single element as a function of ¢ where k is a constant (Q m~') involving the distance D and 1, a



current. Equation (1) is the absolute field pattern in the horizontal plane. It is



ST,._-_OOH_— independent of ¢ so that the relative pattern is a circle as indicated in Fig. 11-25.



" In the so-called “broadside case” (here is always a major lobe of radiation broadside to the array, fl Next let the elements be replaced by isotropic point sources of equal ampli-



although at large spacings there may be an end-fire lobe of equal magnitude (as, for example, when | tude. The pattern £,,,(¢) as a function of ¢ in the horizontal plane for two such



the spacing is 14). isotropic in-phase point sources is given by (4-2-6) as



7'In the so-called “end-fire case” the pattern always has zero radiation broadside. The maximum



radiation is always end-fite if the spacing is 4/2 or less. However, for greater spacings the maximum d, cos ¢



radiation is, in general, not end-fire. Since spacings of i/2 or less are of principal interest, the array EA) = 2Ey cos ae Q)



may be referred to as an end-fire ype.



438 1 ARRAYS OF DIPOLES AND OF APERTURES 11-2 ARRAY GF TWO DRIVEN 1/2 ELEMENTS. BROADSIDE cast 439



where d, is the distance between sources expressed in radians; that is, ;



ee salicati q i 3 Vy



Applying the principle of pattern multiplication, we may consider that Ey is the



field intensity from a single element at a distance D. Thus, 5



Eq = E_n(ψ) = kh, 44) point for



Introducing (4) into (2) yields the field intensity £(p) as a function of in the ’ 2



horizontal plane at a large distance D from the array, or Figure 11-3 Broadside array of 2 linear 4/2 ele-



| To transmitter ments with arrangement for driving elements with



d, COS d, cos equal in-phase currents.



E(φ) = E,(¢)2 cos (e<2) = 2kI, cos (i=) (5)



This expression may be called the absolute field pattern in the horizontal plane. q 11-2b Driving-Point Impedance. Suppose that the array is energized by the



The electric field at points in this plane is everywhere vertically polarized. The transmission-line arrangement shown in Fig. 11-3. Two transmission lines of



shape of this pattern is illustrated in Fig. t1-2c, and also partially in Fig. 11-2a, H equa! length | join at P to a third line extending to a transmitter. Let us find the



for the case where d = 4/2. The maximum field intensity is at ¢ = 90° or broad- driving-point impedance presented to the third line at the point P.' This will be



side to the array. . . | called the driving point for the array,



The field intensity £,(6) as a function of 8 ‘on a single 2 Sement ata Let V, be the emf applied at the terminals of element 1. Then



dist: i vertical plane (yz plane in Fig. 11-2a) is, from (5-5-12), given b:



stance D in the vertical plane (yz pl 8. given by W=hZy4+hZi (9)



E,(0) = kL, ses Lee eet) (6) where J, is the current in element 1, /, the current in element 2, Z,, is the



sin self-impedance of element t and Z,, is the mutual impedance between the two



The shape of this pattern is shown in Fig. 11-2d. It is independent of the angle ¢. elements. Likewise, if V, is the emf applied at the terminals of element 2,



The pattern £,,,(@) in the’ vertical plane for two isotropic sources in place of the Vy = 1g 222 +N Zay (10)



two elements is where Zz = the self-impedance of element 2



Ex} = 2Eo (7a) The currents are equal and in phase so



Applying the principle of pattern multiplication, we put heh an



Ey = E,(0) (7b) Therefore, (9) and (10) become



so that the field intensity E(@) in the vertical plane at a distance D from the array V, =1;(Z,; + Z12) (12)



* and Vz = h@ar + Z12) (13)



H(@) = 2k, con Meith oe (8) The terminal impedance Z, of element 1 is



This may be called the absolute field pattern in the vertical plane. This pattern has Z,= ion Zun+2i (14)



the same shape as the pattern for a single element in the vertical plane and is



independent of the spacing. The relative pattern is presented in Fig. 11-2e and



also partially in Fig. 11-2a. The relative 3-dimensionat field variation for the case GH. Brown, “A Critical Stody of the Characteristics of Broadcast Antennas as Affected by



where d = 4/2 is suggested in Fig. 11-2a. This pattern is actually bidirectional, Antenna Current Distribution,” Proc. IRE, 24, 48-81, January 1936.



only half being shown. G.H. Brown, “ Directional Antennas,” Proc. IRE, 25, 78-145, January 1937. '



112 ARRAY OF TWO DRIVEN i22 ELEMENTS. BROADSIDE case 441



440 11 ARRAYS OF DIPOLES AND OF APERTURES



pattern integration as in Chap. 3, but with self- and mutual-impedance values



and the terminal impedance Z, for element 2 is available a shorter method is as follows.



Let the total power input (real power) to the array be P.' Assuming no heat



Ze a =Zy+Zi (sy losses, the power P, in element | is



identical Py = HR, + Ria) (19)



ince the elements are identical ; :



Since and the power P, in element 2 is



Therefore, the terminal impedances given by (14) and (15) are equal; that is, q 2 = 1YAR22 sa) (20)



"7 where J, and 7, are rms currents. However, R,2 = Ry, and I, = 1,. Making



Zy=2,=2y +2 i) these substitutions and adding (19) and (20) to obtain the total power P, we have



Since Z, = Z, and J, = I, it is necessary that the emf V, applied at the terminals P=P,+P,=2P(R R



of element 1 be equal and in phase with respect to the emf V, applied at the f ut Pz = 24(R,, + Riad (21)



terminals of element 2. and he P (22)



For the case where the spacing d is 7/2, the terminal impedance Z, of each = RD +R)



_ 7 . uppose that we express the gain with respect to a single 4/2 clement as the



Zs Za + Zir= Ru + Riz +X + Xa) reference antenna. Let the same power P be supplied to this antenna, Then



73 — t3 + (43 — 29) q assuming no heat losses, the current /, at its terminals is



=60+jl4 2 (18) 1 P 3)



Suppose that the reactance of 14 Q is tuned out at the terminals by a series Roo



capacitance.’ The terminal impedance then becomes a pure resistance of 60 Qif where Rog is the self-resistance of the reference antenna (=R,,).



the length / of each transmission line between the antenna terminals and P is 2/2, In general, the gain in field intensity? of an array over a reference antenna is



the driving-point impedance of the array at P is @ pure resistance of 300. This given by the ratio of the field intensity from the array to the field intensity from



value is independent of the characteristic impedance of the 4/2 lines. However, a the reference antenna when both are supplied with the same power P, The com-



resistance of 30 Q is too tow to be matched readily by an open-wire transmission a parison ‘is, of course, made in the same direction from both the array and the



line, Therefore, a more practical arrangement would be ‘0 make a caval ie Ha reference antenna. In the present case it will be convenient to obtain two gain



Bee ite aye a eo 0? can expressions, one for the horizontal plane and the other for the vertical plane.



let the characteristic impedance of each 4/4 line tines are ted; In the horizontal plane the field intensity Ej,(#), as a function of g, at a



line transforms the 60 & to 1200 9 and since two such lines are connected in distance D from a single vertical center-fed 4/2 reference antenna is of the form of



paralle] at P, the driving-point impedance for the array is a pure resistance of (1). Thus,



600 Q. This is the impedance presented to the line to the transmitter. For an



impedance match this line should have a characteristic impedance of 600 2. E ) = ki, (24)



11-2c Gain in Field Intensity. As the last part of the analysis of the array, let



us determine the gain in field intensity for the array. This could be done by



3 * It is important that the antenna power P be considered constant. Most transmitters are essentially



constant power devices which can be coupled to a wide ratige of antenna impedance. Until the



ee antenna power was considered constant by G. H. Brown (Proc. IRE, January 1937) the advantages of



" It is often simpler to resonate the elements by shortening them slightly. This modifies the resistive closely spaced elements were not apparent. Prior to this time the antenna current had usually been



component of the impedance and also alters the £(@) field pattern, but to a first approximation these q considered constant.



effects can usually be neglected 3 2 The power gain discussed in Chap. 2 is equal to the square of the gain in field intensity. The power



? For the special case of @ 2/4 line, the general: transmission-line formufa reduces to Z,, = Z3/Z, gain is the ratio of the radiation intensities (power per unit solid angle) for the array and reference



where Z,, is the input impedance, Z, the charatteristic impedance and Z, the load impedance. Thus, antennas, the radiation intensity being proportional to the square of the field intensity.



44211 ARRAYS OF DIPOLES AND.OF APERTURES 112 ARRAY OF TWO DRIVEN 22 ELEMENTS. BROADSIDE case 443



where I, is the terminal current and “HW” indicates “Half-Wavelength (7/2) @- 180°



antenna.” Substituting the value of fy from (23), we obtain



Ewu() =k [2 (25) a = 124°



The field intensity E(@) in the horizontal plane at a distance D from the array is o= 90% 9-90"



given by (5). Introducing the’ vatue of the terminal current /, from (22) into (5) - :



E(g) =k (“Se a 608 (26) o- -56 .



The ratio of (26) to (25) gives the gain in field intensity of the array (as a function q H oo



of ¢ in the horizontal plane) with respect to a vertical 4/2 reference antenna with .



ena wa ‘ Figure 11-4 Horizontal plane pattern of broadside array of 2 vertical in-phase 4/2 elements spaced



the same power input. This gain will be designated by the symbo! G(@)[A/HW] JD The pattern of a single vertical 4/2 reference antenna with the same power input is shown for



where the expression in the brackets is by way of explanation that it is the gain in comparison.



field of the array (A) with respect to a half-wavelength reference antenna (HW)! in



the same direction from both array and reference antenna. Thus,



! It is also of interest to find the angle θ» for which the gain is unity. For this



A E(p) 2Roo d, cos q condition (28) becomes



G. El =e = eo 81 (27)



HOH Fw | > Eye) ~ VR + Rua 2 .



oo, cos ( cos 9) = 0.64 (29)



The absolute value bars || are introduced so that the gain will be confined to 2



positive values (or zero) regardless of the values of d, and ¢. A negative gain q or bo = +56" or +124"



would merely indicate a phase difference between the fields of the array and the 4 . ~



reference antenna. These angles are shown in Fig. 11-4. The array has a gain of greater than unity in



If the gain is the ratio of the maximum field of the array to the maximum ! both broadside directions over an angle of 68°.



field of the reference antenna, it is designated by G, (not a function of angle). The gain as a decibel ratio is given by the relation



The self-resistances Roy = Ri, = 73 Q. For the case where the spacing is Gain = 20 fog, G dB)



J{2, d, = mand Ry, = —13 so that (27) becomes B10 Gr (AB)



where G, = gain in field intensity



G 40| si | = 1.56 cos G cos ) (28) Thus, a field-intensity gain of 1.56 is equal to 3.86 dB.



4 Turning our attention now to the gain in the vertical plane (yz plane of



In the broadside direction (ψ = π/2), the pattern factor becomes unity. The gain} Fig. 11-2a), the field intensity Eyw(6) as a function of @ in this vertical plane at



is then 1.56. This is the ratio of the maximum field of the array to the maximum distance D from a single vertical 4/2 reference antenna with the same power input



field of the reference antenna (see Fig. 11-4). Hence, G, = 1.56. is of the form of (6). Thus,



Eqd0) = ky S28 L272) cos 81 30)



where I, = the terminal current



‘ Both the array and the 2/2 reference antenna are assumed to be in free space. Thus, to be more ee



explicit, the expression G{p)[AFS/HWFS], meaning the gain in field intensity of the Array in Free Substituting its value from (23), we get



Space (AFS) with respect to a Half-Wavelength reference antenna in Free Space (HWES), might be]



used. However, to simplify the notation, the letters “FS” will be omitted when both antennas are in E =~ [Pos [(2/2} cos 6] G1)



free space. awl®) = Roo sin 6



444 11 ARRAYS OF DIPOLES AND OF APERTURES



11-3 ARRAY OF 2 DRIVEN 12 ELEMENTS ENDFIRE case 445



Figure 11-5 Vertical-plane pattern 4



of broadside array of 2 vertical in- 5



phase i/2 elements spaced 4/2. The



Antenna pattern of a single vertical 4/2 refer



elements ence antenna with the same power



input is shown for comparison.



j Figure 11-6 End-fire array of 2 linear 4/2 elements with currents of



equal magnitude but opposite phase.



- : ; field intensity of the array with respect to an isotropic source is



The field intensity E(0) as a function of @ in the vertical plane at a distance D



from the array is given by (8). Introducing the value of the terminal current J, G | = 1.56 x \/1,64 = 2.0 (or 6.0 dBi)! (35)



from (22) into (8}, we have iso.



This value is in the broadside direction (@ = 6 = 90°).



FI) =k {_2P___ cos [(n/2) cos 8] (2)



Rut Ri sin @ 11-3 ARRAY OF 2 DRIVEN 4/2 ELEMENTS. END-FIRE



CASE, Consider an array of 2 center-fed vertical 4/2 elements (dipoles) in free



The ratio of (32) to (31) gives the gain in field intensity, G{@)[A/HW], of the space arranged side by side with a spacing d and equal currents in opposite phase



array as a function of @ in the vertical plane over a vertical 7/2 reference antenna as in Fig. 11-6. The only difference between this case and the one discussed in



with the same power input. Thus, Sec. 11-2 is that the currents in the elements are taken to be in the opposite phase



instead of in the same phase. As in Sec. 11-2, the analysis wilt be divided into 3



6 of A ] E(0) 2Roo Ga subsections on the field patterns, driving-point impedance and gain in field inten-



Gwl=-poa= Je 7 RD sity.



41 aw |” Eww)” VR + Rea %



. h here the 11-3a Field Patterns. The field intensity £,(#) as a function of at a distance



The gain is a constant, being independent of the angle 9. For the case where t Din a horizontal plane (xy or @ plane in Fig. 11-7a) from a single element is



spacing is 4/2, (33) becomes



A where k = a constant involving the distance D -



60) | 1-56 (or 3.86 dB) G4) 1, = the terminal current



, Replacing the elements by isotropic point sources of equal amplitude, the pattern



The shape of the pattern for the array and for the 4/2 reference antenna is the E,,.(¢) in the horizontal plane for two such isotropic out-of-phase sources is given



same as shown in Fig. 11-5, but the ratio of the radius vectors in a given direc- by (4-2-10) as.



tion is a constant equal to 1.56. q



If the reference antenna is an isotropic source instead of a 2/2 antenna, the Eu) = 2Ep sin (=) w



gain in the, vertical plane is a function of the angle θ. The maximum gain in field a 2



intensity of the array over an isotropic source with the same power input



is ./1.64 times greater than the voltage gain over a A/2 reference antenna —



[D(i/2)} = 1.64, see Sec. 2-24}. Thus, when the spacing is 4/2, the maximum gain in " Distinguish between “dB” for gain with respect to a reference antenna (2/2 dipole in the present



case) and “ dBi” for gain with respect to an isotropic source.



4461. ARRAYS OF DIPOLES AND OF APERTURES V3 ARRAY OF 2 DRIVEN i2 ELEMENTS END-FIRE CASE 447



z The field intensity E,() as a function of @ from a single 4/2 element at a



4 distance D in the verticat plane (xz plane in Fig. 11-7a) is, from (5-5-12), given by



<| The pattern £,,,(9) as a function of @ in the vertical plane, for two isotropic



£0) Ya Y Y sources in place of the two elements is, from (4-2-10),



(7 IN E,s{6) = 2Eo sin (SEP ™ 6)



ce! SAT Note that @ is complementary to ¢ in (4-2-10), so cos ¢ = sin 0.



aes Putting Ey = E,(0), the field intensity £(6) as a function of 8 in the vertical



4 plane at a large distance D from the array is



) ayy, C08. LH/2) 608 A] (ad, sin 6



E(@) = 2ki, ine sin 2 (6)



z This is the absolute field pattern in the vertical plane. The relative pattern is



Eto) 4 Ew) illustrated in Fig. 1t-7c, and also partially in Fig. 11-7a, for the case where the



spacing is 7/2. The relative 3-dimensional field variation for this case (d = 4/2) is



suggested in Fig. 11-7a. This pattern is actually bidirectional, only half being



y ; 11-3b Driving-Point Impedance. Let V, be the emf applied to the terminals



® © of element 1. Then



Figure 11-7 Patterns for end-fire array of 2 linear out-of-phase 2/2 elements with spacing ¢ = 1/2. WaHh2n+he2y. (7)



Likewise, if V, is the emf applied to the terminals of element 2,



sder that Ea the Y= h2nth2u 8)



Applying the principle of pattern multiplication, we may consider that Ep is tl . . ae



field intensity from a single element at a large distance D. Thus The currents are equal in magnitude but opposite in phase so



Eo = E\(@) = Ky e Therefore, (7) and (8) become



and the field intensity (@) as a function of @ in the horizontal plane at a large | Y= NZ — Zag) (10)



distance D from the array is



and ¥, = TAZ. — Z,2) ay



(6) = 2kt, sin (34) 8) ‘The terminal impedance Z, of element 155



This is the absolute field pattern in the horizontal plane. The electric field at Zap Zn -2u (12)



points in this plane is everywhere vertically polarized. The relative pattern for the 5 .



case where the spacing d is 4/2 is shown in Fig. 11-7 and also partially in and the terminal impedance 2, of element 2 is



Fig. 11-7a. The maximum field intensity is at = 0° and ¢ = 180° Hence, the hh



j * ” 2,27 =2n-Z2 (13)



array is commonly referred to as an “ end-fire” type. . fy



44811 ARRAYS OF DIPOLES AND OF APERTURES 114 ARRAY OF 2 DRIVEN 42 ELEMENTS 449



—« ancy rleronce | eee



point or Ss Elements



Figure 11-8 End-fire array of 2 linear 4/2 elements



To transihitter with arrangement for driving elements with currents Figure 11-9 Horizontal plane pattern (a) aid vertical plane pattern (b) of end-fie array of 2 vertical



of equal magnitude but opposite phase. 2/2 elements with 4/2 spacing. The patterns of a vertical 4/2 reference antenna with the same power



input are shown for comparison.



Therefore, obtained by substituting (17) in (3) and (aking the ratio of this result to (11-2-25).



2, =Z,=Z 4-212 (14) This yields



or taf (15) A|_ {_2Roo | 5, (4008 & 18)



ob CON WIV Ry — Ra 2 (



Since 1; = —J, it follows from (15) that V, = —¥,. This means that the 2 ele- For a spacing of 7/2, (18) reduces to



ments must be energized with emfs which are equal in magnitude and opposite in



phase. This may be done by means of a crossover in the transmission line from. 646) 50 = 13| sin [@) cos φ (19)



the driving point P to one of the elements as shown in Fig. 11-8. The length / of HW 2,



each line is the same. In the end-fire directior ° ¥ it



. wars 1 ns (¢ = 0° and 180°) the pattern factor becomes unity, and



For the case where the spacing between elements is 4/2, the terminal imped- the gain is 1,3 or 2.3 dB. This is the gain G, (see Fig, 11-9).



ance of each element is The gain in field intensity G(@[A/HW] as a function of @ in the vertical



Z,=Ry,— Ri + HX, — Xd plane (xz plane of Fig. 11-7a) with respect to a 4/2 reference antenna is found by



=864j72 2 (16) substituting (17) in (6) and taking the ratio of this result to (11-2-31), obtaining



Consider that the reactance of 72 Q is tuned out by a series capacitance at the G 0) oy = {_2Roo_ sin (2)| 20)



terminals of each element. The termina! impedance is then a pure resistance of HW. Ru —Ri 2



86 ©. To obtain a driving-point resistance of 600 Q, let the length | of the line which is of the same form as the gain expression (18) for the horizontal plane



from P to each element be 4/4 and let the line impedance be ,/1200 x 86 = {note that maximum radiation is in a direction @ = 90°, ¢ = 0°).



321. For an impedance match, the line from the driving point P to the trans- The gain in field intensity G, of the array over an isotropic source with the



mitter should have a characteristic impedance of 600 Q. same power input is 1.3 x \/1.64 = 1.66 (or 4.4 dBi).



11-3e Gain in Field Intensity, Using the same method as in See: 11-2c, the 114 ARRAY OF 2 DRIVEN i/2 ELEMENTS. GENERAL CASE



current 1, in each clement for a power inp! Is given DY WITH EQUAL CURRENTS OF ANY PHASE RELATION.’ In the



P preceding sections 2 special cases of an array of two 2/2 driven elements have



It is assumed that there are no heat losses. The current I in a single 4/2 reference \ For a more detailed discussion of this case and also of the most general case where the current



antenna is given by (11-2-23). The gain in field intensity G {¢)[A/HW] as a func- amplitudes are unequal, see G. H. Brown, “Directional Antennas.” Proc. IRE, 28, 78-145, January



tion of @ in the horizontal plane with respect to a 4/2 reference antenna is | 1937.



450 1) ARRAYS OF DIPOLES AND OF APERTURES (14 ARRAY OF 2 DRIVEN 42 ELEMENTS 451.



where «=the phase angle of the mutual impedance Z,, (that is, t = arctan



Xy+/Riz where Z,2 = Ryz + jX42)



Element 1 Therefore, the power P, in element 1 is



\ pfemen? Py =H PR, = 1, PLRiy + 1Z12| cos (& + 9)] (10)



Figure 11-10 Array of 2 side-by-side elements i i



|__u—_..| aeclie plane cfoaee and the power P, in element 2 is



P2 = [42 [Raz + |Z12| cos (x — 8)] (14)



been treated. In one case the currents_in the elements are in phase (phase Since R,, = R22, the total power P is



difference = 0°) and in the other the currents are in opposite phase (phase



difference = 180°), In this section the more general case is considered where the PHP, + Po =H, /{2Rus + (Zy2|[e08 (t + 6) + cos (r — )}}



phase difference may have any value. As in the preceding cases, the two 2/2 = 211, PRyy + [Zig] cos t cos 8)



elements are arranged side by -ide with a spacing d and are driven with currents ;



of equat magnitude. = 217, |(Rir + Riz cos 5) (12)



For the general-phase case the radiation-field pattern in the horizontal It follows that the gain in field intensity as a function of @ in the horizontal



plane (xy plane of Fig. 11-7a) is, from (4-2-20), given by plane! of the array over a single 4/2 clement with the same power input is



y A 2R, d, cos @ + 6



E(#) = 2kI, cos = 1) G (a = /———4_ — 13)



1) = 2kdy cos 5 ‘ ‘AW aw ]~ y Ry + Riz cos 6 | °° 2 0)



where y is the total phase difference between the fields from element 1 and ele- A polar plot of (13) with respect to the azimuth angle ¢ gives the radiation-field



ment 2 at a large distance in the direction ¢ (see Fig. 11-10). Thus, pattern of the array in the horizontal plane, the ratio of the magnitude of the



=d 5 Q) radius vector to a unit radius indicating the gain over a reference 4/2 antenna.



Y= 4, cos b+ Brown? has calculated such patterns as a function of phase difference 5 and



where 5 = the phase difference of the currents in the elements spacing d,. Examples of these are shown in Fig, 11-11.



A positive sign in (2) indicates that the current in element 2 of Fig. 11-10 is th The caclation-feld attern in the vertical plane containing the elements (in



advanced in phase by an angle 5 with tespect to the current in element 1; that is, ¢ plane of the page of Fig. 11-12) is



Lah ls £{0) = 2k1, cos (42 8i0.9 + 2) £08 Ln/2) cos 8] 4

## 中文翻译

> **中文：** 第8章介绍**缝隙天线(Slot Antennas)**。缝隙天线利用导电面上的窄缝辐射电磁波，基于巴俾涅原理(Babinet's Principle)与偶极子天线互补——缝隙的辐射特性与等尺寸偶极子的辐射特性呈互补关系。

### 8-1 缝隙天线基本理论
根据巴俾涅原理，理想导电无限大平面上的窄缝天线与互补偶极子天线具有互补的阻抗和方向图特性：
- 缝隙的电场方向图与互补偶极子的磁场方向图相同
- 缝隙阻抗$Z_{\text{slot}}$与互补偶极子阻抗$Z_{\text{dipole}}$满足$Z_{\text{slot}} \times Z_{\text{dipole}} = \eta^2/4$，其中$\eta = 377\ \Omega$为自由空间本征阻抗

### 8-2 常见缝隙天线
- **半波缝隙天线**：辐射电阻约500-1000 $\Omega$，方向图与半波偶极子互补
- **波导缝隙阵**：在波导壁上的缝隙阵列，用于高方向性雷达和通信天线
- **谐振式和非谐振式缝隙阵**

### 8-3 应用
缝隙天线广泛应用于机载雷达、波导缝隙阵（如机载预警雷达）、微波通信和卫星天线，特点是低剖面、易与飞行器表面共形。

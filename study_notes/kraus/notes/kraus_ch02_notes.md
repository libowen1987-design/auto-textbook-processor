# Kraus《Antennas》2nd Edition — Chapter 2

> **中英双语版**

## Chapter 2: Basic Antenna Concepts

> **中文：** 本章介绍天线的核心基本概念：定义（天线作为导波与自由空间波的过渡区域）、基本参数（辐射电阻、天线温度、方向图）、波束面积、辐射强度、方向性、增益、孔径概念及各种孔径的定义与关系。

2-1 INTRODUCTION. The purpose of this chapter is to provide introductory insights into antennas and their characteristics. Following a section on definitions, the basic parameters of radiation resistance, temperature, pattern, directivity, gain, beam area and aperture are introduced. From the aperture concept it is only a few steps to the important Friis transmission formula. This is followed by a discussion of sources of radiation, field zones around an antenna and the effect of shape on impedance. The sources of radiation are illustrated for both transient (pulse) and continuous waves. The chapter concludes with a discussion of polarization and cross-field.

> **中文：** 本章目的：提供天线及其特性的入门知识。将介绍辐射电阻、天线温度、方向图、方向性、增益、波束面积和孔径等基本参数，并推导Friis传输公式。随后讨论辐射源、天线周围场区和形状对阻抗的影响，最后讨论极化和交叉场。

2-2 DEFINITIONS. A radio antenna may be defined as the structure associated with the region of transition between a guided wave and a free-space wave, or vice versa.

In connection with this definition it is also useful to consider what is meant by the terms transmission line and resonator.

A **transmission line** is a device for transmitting or guiding radio-frequency energy from one point to another. Usually it is desirable to transmit the energy with a minimum of attenuation, heat and radiation losses being as small as possible. Thus, the wave transmitted along the line is 1-dimensional in that it does not spread out into space but follows along the line.

A **generator** connected to an infinite, lossless transmission line produces a uniform traveling wave along the line. If the line is short-circuited, the outgoing traveling wave is reflected, producing a standing wave on the line due to the interference between the outgoing and reflected waves. A standing wave has associated with it local concentrations of energy. If the reflected wave is equal to the outgoing wave, we have a pure standing wave. The energy concentrations in such a wave oscillate from entirely electric to entirely magnetic and back twice per cycle. Such energy behavior is characteristic of a resonant circuit, or **resonator**. Where there is only an outer conductor, as in a short-circuited section of waveguide, the device is called a **cavity resonator**.

Thus, antennas radiate (or receive) energy, transmission lines guide energy, while resonators store energy.

A guided wave traveling along a transmission line which opens out, as in Fig. 2-1, will radiate as a free-space wave. The guided wave is a plane wave while the free-space wave is a spherically expanding wave. The region of transition between the guided wave and the free-space wave may be defined as an antenna.

While transmission lines (or waveguides) are usually made so as to minimize radiation, antennas are designed to radiate (or receive) energy as effectively as possible.

The antenna, like the eye, is a transformation device converting electromagnetic photons into circuit currents; but, unlike the eye, the antenna can also convert energy from a circuit into photons radiated into space. In simplest terms: an antenna converts photons to currents or vice versa.

Consider a transmission line connected to a dipole antenna. The dipole acts as an antenna because it launches a free-space wave. However, it may also be regarded as a section of an open-ended transmission line. In addition, it exhibits many of the characteristics of a resonator, since energy reflected from the ends of the dipole gives rise to a standing wave and energy storage near the antenna. Thus, a single device, in this case the dipole, exhibits simultaneously properties characteristic of an antenna, a transmission line and a resonator.

> **中文：** 天线定义为导波与自由空间波之间的过渡区域。传输线引导能量（一维），天线辐射能量（三维），谐振器存储能量。偶极子天线同时具有天线、传输线和谐振器的特性。光子是电磁能量的量子单位，天线实现光子和电路电流之间的转换。

2-3 BASIC ANTENNA PARAMETERS. Referring to Fig. 2-2, the antenna appears from the transmission line as a 2-terminal circuit element having an impedance $Z$ with a resistive component called the **radiation resistance** $R_r$.

The radiation resistance $R_r$ is not associated with any resistance in the antenna proper but is a resistance coupled from the antenna and its environment to the antenna terminals.

Associated with the radiation resistance is also an **antenna temperature** $T_A$. For a lossless antenna this temperature has nothing to do with the physical temperature of the antenna proper but is related to the temperature of distant regions of space (and nearer surroundings) coupled to the antenna via its radiation resistance. In this sense, a receiving antenna may be regarded as a remote-sensing, temperature-measuring device.

Both the radiation resistance $R_r$ and the antenna temperature $T_A$ are single-valued scalar quantities. The radiation patterns, on the other hand, involve the variation of field or power as a function of the two spherical coordinates $\theta$ and $\phi$.

> **中文：** 天线在传输线端表现为阻抗$Z$，其电阻分量称为辐射电阻$R_r$（非欧姆损耗，而是与空间耦合的等效电阻）。天线温度$T_A$反映天线通过辐射电阻"看到"的远方空间温度，接收天线可视为遥感测温装置。方向图则描述场/功率随球坐标$(\theta, \phi)$的变化。

2-4 PATTERNS. Figure 2-3a shows a field pattern where $r$ is proportional to the field intensity at a certain distance from the antenna in the direction $(\theta, \phi)$. The pattern has its main-lobe maximum in the $z$ direction ($\theta = 0$) with minor lobes (side and back) in other directions. Between the lobes are nulls in the directions of zero or minimum radiation.

To completely specify the radiation pattern with respect to field intensity and polarization requires three patterns:
1. The $\theta$ component of the electric field as a function of the angles $\theta$ and $\phi$: $E_\theta(\theta, \phi)$ (V m$^{-1}$)
2. The $\phi$ component of the electric field as a function of the angles $\\theta$ and $\phi$: $E_\phi(\theta, \phi)$ (V m$^{-1}$)
3. The phases of these fields as a function of the angles $\theta$ and $\phi$: $\delta_\theta(\theta, \phi)$ and $\delta_\phi(\theta, \phi)$ (rad or deg)

The normalized field pattern is $E_n(\theta, \phi) = E_\theta(\theta, \phi) / E_\theta(\theta, \phi)_{\text{max}}$.

The normalized power pattern is $P_n(\theta, \phi) = S(\theta, \phi) / S(\theta, \phi)_{\text{max}}$, where $S = |E|^2 / Z_o$, and $Z_o = 376.7\ \Omega$ is the intrinsic impedance of space.

Patterns can be presented in decibels: $P_n(\theta, \phi)_{\text{dB}} = 10 \log_{10} P_n(\theta, \phi)$ (dB).

> **中文：** 方向图主瓣最大值在$z$方向，其余方向有副瓣和背瓣，瓣间为零点。完整描述需三个方向图：$E_\theta(\theta,\phi)$、$E_\phi(\theta,\phi)$及相位$\delta_\theta,\delta_\phi$。归一化场方向图$E_n = E/E_{\text{max}}$，功率方向图$P_n = S/S_{\text{max}} \propto |E|^2$。可用dB标度显示副瓣细节。

2-5 BEAM AREA (OR BEAM SOLID ANGLE). The arc of a circle subtends an angle. The area of the surface of a sphere as seen from the center of the sphere subtends a **solid angle** $\Omega$ (sr). The total solid angle subtended by the sphere is $4\pi$ steradians.

The incremental area $dA$ of the surface of a sphere is given by
$$dA = (r \sin\theta\, d\phi)(r\, d\theta) = r^2 \sin\theta\, d\theta\, d\phi = r^2\, d\Omega \tag{1}$$
where $d\Omega = \sin\theta\, d\theta\, d\phi$ is the incremental solid angle.

The area of the sphere is $A_{\text{sphere}} = 2\pi r^2 \int_0^\pi \sin\theta\, d\theta = 4\pi r^2$.

Thus, $1\text{ steradian} = 1\text{ sr} = (\text{solid angle of sphere}) / 4\pi = (180/\pi)^2 = 3282.8064 \text{ square degrees}$.
And $4\pi$ steradians $= 3282.8064 \times 4\pi = 41252.96 = 41253 \text{ square degrees}$.

The **beam area** (or beam solid angle) $\Omega_A$ for an antenna is:
$$\Omega_A = \iint_{4\pi} P_n(\theta, \phi)\, d\Omega \quad (\text{sr}) \tag{5}$$

The beam area $\Omega_A$ of an actual pattern is equivalent to the solid angle subtended by the spherical cap of a cone-shaped pattern.

Often $\Omega_A \approx \Theta_{\text{HP}} \Phi_{\text{HP}}$, where $\Theta_{\text{HP}}$ and $\Phi_{\text{HP}}$ are the half-power beam widths (HPBW) in the two principal planes.

> **中文：** 立体角$\Omega$（单位：球面度sr）是球面面积对球心所张的角度。球面总面积$4\pi$ sr = 41253平方度。天线的波束面积$\Omega_A = \iint P_n(\theta,\phi) d\Omega$，可近似为$\Omega_A \approx \Theta_{\text{HP}} \Phi_{\text{HP}}$（两个主平面半功率波束宽度的乘积）。

2-6 RADIATION INTENSITY. The power radiated from an antenna per unit solid angle is called the **radiation intensity** $U$ (W sr$^{-1}$). The normalized power pattern can be expressed as $P_n(\theta,\phi) = U(\theta,\phi) / U(\theta,\phi)_{\text{max}}$. While the Poynting vector $S$ depends on distance ($\propto 1/r^2$), the radiation intensity $U$ is independent of distance (in the far field).

> **中文：** 辐射强度$U$是单位立体角内的辐射功率（W/sr），在远场区与距离无关。

2-7 BEAM EFFICIENCY. The total beam area $\Omega_A$ consists of the main beam area $\Omega_M$ plus the minor-lobe area $\Omega_m$:
$$\Omega_A = \Omega_M + \Omega_m \tag{1}$$

The **beam efficiency** is $\varepsilon_M = \Omega_M / \Omega_A$.
The **stray factor** is $\varepsilon_m = \Omega_m / \Omega_A$, with $\varepsilon_M + \varepsilon_m = 1$.

> **中文：** 波束效率$\varepsilon_M = \Omega_M / \Omega_A$（主瓣能量占比），杂散因子$\varepsilon_m = \Omega_m / \Omega_A$（副瓣能量占比），两者之和为1。

2-8 DIRECTIVITY. The **directivity** $D$ of an antenna is the ratio of the maximum radiation intensity $U(\theta,\phi)_{\text{max}}$ to the average radiation intensity $U_{\text{av}}$ (averaged over a sphere):
$$D = \frac{U(\theta,\phi)_{\text{max}}}{U_{\text{av}}} = \frac{S(\theta,\phi)_{\text{max}}}{S_{\text{av}}} \tag{1}$$

In terms of power pattern,
$$D = \frac{4\pi}{\iint_{4\pi} P_n(\theta,\phi)\, d\Omega} = \frac{4\pi}{\Omega_A} \tag{3,4}$$

Thus, the smaller the beam solid angle, the greater the directivity.

> **中文：** 方向性$D$=最大辐射强度/平均辐射强度=$4\pi/\Omega_A$，波束面积越小，方向性越强。

2-9 EXAMPLES OF DIRECTIVITY. If an antenna were isotropic ($P_n(\theta,\phi)=1$ for all $\theta,\phi$), then $\Omega_A = 4\pi$ and $D = 1$.

Neglecting the effect of minor lobes, a simple approximation is:
$$D \approx \frac{4\pi}{\Theta_{\text{HP}} \Phi_{\text{HP}}} = \frac{41253}{\Theta_{\text{HP}}^\circ \Phi_{\text{HP}}^\circ} \tag{4}$$

If HPBWs are both $20^\circ$:
$$D \approx \frac{41253}{20 \times 20} \approx 103 \approx 20\ \text{dBi}$$

> **中文：** 理想各向同性天线$D=1$。忽略副瓣时$D \approx 41253/(\Theta_{\text{HP}}^\circ \Phi_{\text{HP}}^\circ)$。若半功率波束宽度$20^\circ \times 20^\circ$，则$D \approx 103 \approx 20\ \text{dBi}$，即主瓣方向辐射功率是各向同性的约100倍。

2-10 DIRECTIVITY AND GAIN. The **gain** $G$ of an antenna depends on both its directivity and its efficiency:
$$G = kD \tag{1}$$
where $k$ = efficiency factor ($0 < k < 1$), accounting for ohmic losses in the antenna.

> **中文：** 增益$G = kD$，效率因子$k$反映天线欧姆损耗（发射时部分功率以热能消耗，未辐射）。当使用单值增益时，通常指最大主瓣增益值。

2-11 DIRECTIVITY AND RESOLUTION. The **resolution** of an antenna may be defined as half the beam width between first nulls (BWFN/2). Resolution $\approx$ HPBW. The number $N$ of point sources an antenna can resolve is:
$$N = \frac{4\pi}{\Omega_A} = D$$
Thus, ideally the directivity equals the number of resolvable point sources.

> **中文：** 天线分辨率$\approx$半功率波束宽度（HPBW）。理想情况下，天线可分辨的点源数$N$等于方向性$D$。

2-12 APERTURE CONCEPT. The aperture concept is introduced by considering a receiving antenna (e.g., an electromagnetic horn) immersed in a uniform plane wave. The power extracted from the wave is proportional to the aperture area $A$: $P = SA$ (W), where $S$ is the power density (Poynting vector). Several types of apertures are defined: effective, scattering, loss, collecting, and physical aperture.

> **中文：** 孔径概念：接收天线从入射平面波中提取的功率$P = SA$，其中$S$为坡印廷矢量（功率密度）。定义多种孔径类型：有效孔径、散射孔径、损耗孔径、收集孔径和物理孔径。

2-13 EFFECTIVE APERTURE. Consider a dipole receiving antenna with terminating impedance $Z_t = R_t + jX_t$ and antenna impedance $Z_a = R_a + jX_a$, where $R_a = R_r + R_L$ (radiation + loss resistance). The power delivered to the load is $P = I^2 R_t$.

The effective aperture $A_e$ (power absorbed / power density) is:
$$A_e = \frac{V^2 R_t}{S[(R_r + R_L + R_t)^2 + (X_a + X_t)^2]} \tag{9}$$

For maximum power transfer (conjugate match: $R_t = R_r + R_L$, $X_t = -X_a$), the effective aperture is:
$$A_e = \frac{V^2}{4S(R_r + R_L)} \tag{12}$$

For a **lossless** antenna ($R_L = 0$) with conjugate match, the **maximum effective aperture** is:
$$A_{\text{em}} = \frac{V^2}{4S R_r} \tag{13}$$

> **中文：** 有效孔径$A_e$是天线从入射波中提取并传递给负载的功率与入射波功率密度之比。共轭匹配时传输功率最大。无耗天线的最大有效孔径$A_{\text{em}} = V^2/(4SR_r)$。

2-14 SCATTERING APERTURE. The power received by an antenna is partly delivered to the load, partly dissipated as heat in the antenna ($R_L$), and partly **reradiated** (scattered) through the radiation resistance $R_r$. The **scattering aperture** $A_s$ is the ratio of reradiated power to incident power density.

Under conjugate match conditions for a lossless antenna, $A_s = A_{\text{em}}$ (equal power reradiated and delivered to load).

For a **resonant short circuit** ($R_t = 0$, $X_t = -X_a$), the reradiated power is 4 times greater: $A_s = 4A_{\text{em}}$.

For an **open circuit** ($Z_t = \infty$), $I = 0$, so $A_s = 0$ and $A_e = 0$.

**Scattering ratio**: $\beta_s = A_s / A_e$ (ranges from 0 to $\infty$).

> **中文：** 散射孔径$A_s$描述天线再辐射（散射）的功率。共轭匹配且无耗时，$A_s = A_{\text{em}}$（散射功率等于负载吸收功率）。谐振短路时散射功率为匹配时的4倍，$A_s = 4A_{\text{em}}$。开路时$A_s = 0$。

2-15 LOSS APERTURE. If $R_L \neq 0$, some power is dissipated as heat in the antenna. The loss aperture $A_L$ relates to this dissipated power:
$$A_L = \frac{P R_L}{S[(R_r + R_L + R_t)^2 + (X_a + X_t)^2]}$$

> **中文：** 损耗孔径$A_L$对应天线欧姆损耗消耗的功率。

2-16 COLLECTING APERTURE. The total power collected by the antenna is the sum of three components. The collecting aperture $A_c$ is:
$$A_c = A_e + A_s + A_L$$

> **中文：** 收集孔径$A_c = A_e + A_s + A_L$，是有效孔径、散射孔径和损耗孔径之和，代表天线从入射波收集的总功率。

2-17 PHYSICAL APERTURE AND APERTURE EFFICIENCY. The **physical aperture** $A_p$ is a measure of the physical size of the antenna. The **aperture efficiency** is:
$$\varepsilon_{\text{ap}} = \frac{A_e}{A_p} \tag{1}$$

$\varepsilon_{\text{ap}}$ cannot exceed unity for large broadside apertures.

> **中文：** 物理孔径$A_p$是天线的实际物理尺寸。孔径效率$\varepsilon_{\text{ap}} = A_e/A_p$，对大口径侧射天线不超过1。

2-18 SCATTERING BY LARGE APERTURES. For a large broadside aperture ($A$, dimensions $\gg \lambda$) matched to a uniform wave, all power incident on the aperture is absorbed over area $A$ while an equal power is forward-scattered, giving a collecting aperture of $2A$.

The intrinsic impedance of free space is $Z_0 = \sqrt{\mu_0/\varepsilon_0} = 376.7\ \Omega$ (pure resistance). A resistive sheet with $377\ \Omega$ per square is called **space cloth** or **Salisbury sheet**.

For a plane wave incident normally on an infinite sheet of space cloth ($E_i = 1$ V/m):
- Transmission coefficient: $\tau = 1/2$, transmitted field $E_t = \tau E_i = 1/2$ V/m
- Reflection coefficient: $\Gamma = -1/2$, reflected field $E_r = -1/2$ V/m

> **中文：** 大口径天线（尺寸$\gg \lambda$）匹配时，入射功率全部被孔径吸收，同时等量功率向前散射，总收集孔径$A_c = 2A$。自由空间本征阻抗$Z_0 = 377\ \Omega$，电阻值为$377\ \Omega/\text{sq}$的材料称为"空间布"(space cloth)。平面波垂直入射时，透射系数$\tau = 1/2$，反射系数$\Gamma = -1/2$。

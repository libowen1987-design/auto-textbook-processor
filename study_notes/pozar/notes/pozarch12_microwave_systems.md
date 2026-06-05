# Pozar Ch12 (4e Ch14) — Introduction to Microwave Systems
> **中英双语版**

> **Note:** This chapter corresponds to **Chapter 14** in Pozar *Microwave Engineering*, 4th Edition.
> It is the capstone chapter, integrating antennas, communications, radar, radiometry, propagation, and applications.

---

## 14.1 System Aspects of Antennas | 天线的系统方面

### 14.1.1 Radiation Field and Power Density | 辐射场与功率密度

The far-field (Fraunhofer region) electric field of an antenna is:
> 天线的远场（夫琅禾费区）电场为：

$$\mathbf{E}(r, \theta, \phi) = \frac{e^{-jkr}}{r} \, \mathbf{F}(\theta, \phi)$$

where $\mathbf{F}(\theta, \phi)$ is the **vector radiation pattern** (units: V). The far-field is locally a TEM plane wave.
> 其中 $\mathbf{F}(\theta, \phi)$ 为**矢量辐射方向图**。远场局部为 TEM 平面波。

**Time-averaged Poynting vector / 时均坡印廷矢量：**

$$\mathbf{S}_{\text{av}} = \frac{1}{2} \text{Re}[\mathbf{E} \times \mathbf{H}^*] = \hat{r} \, \frac{|\mathbf{E}|^2}{2\eta} \quad \text{[W/m}^2\text{]}$$

### 14.1.2 Radiation Pattern Parameters | 辐射方向图参数

| Parameter | Definition | Description |
|-----------|------------|-------------|
| **Directivity $D$** | $D(\theta,\phi) = \frac{4\pi U(\theta,\phi)}{P_{\text{rad}}}$ | 指向性：特定方向辐射强度与平均辐射强度之比 |
| **Gain $G$** | $G(\theta,\phi) = \frac{4\pi U(\theta,\phi)}{P_{\text{in}}}$ | 增益：考虑天线效率 $\eta_{\text{ant}} = P_{\text{rad}}/P_{\text{in}}$ |
| **Efficiency $\eta_{\text{ant}}$** | $\eta_{\text{ant}} = P_{\text{rad}}/P_{\text{in}}$ | 天线效率：辐射功率与输入功率之比 |

**Friis transmission formula / Friis 传输公式：**

$$P_r = P_t \frac{G_t G_r \lambda^2}{(4\pi R)^2}$$

> 接收功率 $P_r$ 与发射功率 $P_t$、发射增益 $G_t$、接收增益 $G_r$、波长 $\lambda$ 和距离 $R$ 的关系。

---

## 14.2 Wireless Communication Systems | 无线通信系统

### 14.2.1 Link Budget | 链路预算

$$P_r (\text{dBm}) = P_t (\text{dBm}) + G_t (\text{dBi}) + G_r (\text{dBi}) - L_{\text{path}} (\text{dB}) - L_{\text{extra}} (\text{dB})$$

where free-space path loss: $L_{\text{path}} = 20\log_{10}(4\pi R/\lambda)$ [dB].
> 其中自由空间路径损耗 $L_{\text{path}} = 20\log_{10}(4\pi R/\lambda)$。

### 14.2.2 Modulation and Detection | 调制与检测

- **AM/ASK**: Amplitude modulation / 幅度调制
- **FM/FSK**: Frequency modulation / 频率调制
- **PSK/QPSK**: Phase shift keying / 相移键控
- **QAM**: Quadrature amplitude modulation / 正交幅度调制

---

## 14.3 Radar Systems | 雷达系统

### 14.3.1 Radar Equation | 雷达方程

$$P_r = \frac{P_t G_t^2 \lambda^2 \sigma}{(4\pi)^3 R^4}$$

where $\sigma$ is the **radar cross section (RCS)** of the target.
> 其中 $\sigma$ 为目标的**雷达散射截面 (RCS)**。

### 14.3.2 Radar Types | 雷达类型

- **Pulse radar**: Transmits pulses, measures time delay for range
  > 脉冲雷达：发射脉冲，测量时延以确定距离
- **CW radar**: Continuous wave, measures Doppler shift for velocity
  > 连续波雷达：测量多普勒频移以确定速度
- **FMCW radar**: Frequency-modulated CW, measures both range and velocity
  > 调频连续波雷达：同时测量距离和速度

---

## 14.4 Radiometry and Remote Sensing | 辐射测量与遥感

Radiometers measure the noise power emitted by objects, related to their physical temperature.
> 辐射计测量物体发射的噪声功率，与物体物理温度相关。

$$P = k T_{\text{ant}} B$$

where $k$ is Boltzmann's constant, $T_{\text{ant}}$ is the antenna temperature, and $B$ is the bandwidth.
> 其中 $k$ 为玻尔兹曼常数，$T_{\text{ant}}$ 为天线温度，$B$ 为带宽。

---

## 14.5 Propagation Effects | 传播效应

- **Atmospheric attenuation / 大气衰减**: Absorption by O$_2$ and H$_2$O molecules
- **Rain attenuation / 雨衰**: Significant above 10 GHz
- **Multipath / 多径**: Reflections from ground and buildings cause fading
- **Fresnel zone / 菲涅尔区**: Clearance requirement for line-of-sight links

---

## 14.6 Microwave Applications | 微波应用

| Application | Frequency Range | Key Parameter |
|-------------|----------------|---------------|
| Cellular (5G) | 24-40 GHz | Data rate |
| Wi-Fi (2.4/5/6 GHz) | 2.4, 5, 6 GHz | Throughput |
| Satellite TV (Ku, Ka) | 12-30 GHz | EIRP, G/T |
| Radar (automotive) | 24, 77 GHz | Range resolution |
| GPS | 1.2, 1.6 GHz | C/A code |
| RFID | UHF, 2.45 GHz | Read range |

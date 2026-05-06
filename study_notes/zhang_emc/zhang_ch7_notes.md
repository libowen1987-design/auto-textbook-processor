# Chapter 7: Typical Spacecraft Electronic Component Selection and Module EMC Design
*Source: Zhang, Spacecraft Electromagnetic Compatibility Technologies (2020), Chapter 7, pp. 212-250*

---

## 7.1 Selection of Typical Electronic Components and Modules | 典型电子元器件与模块选择

**From the source:** *"The selection of electronic components directly affects the EMC performance of the equipment. Components with lower emissions and higher immunity should be preferred."*

### 7.1.1 Resistors | 电阻器

**From the source:** *"Resistors are the most commonly used electronic products, which can be divided into three types by material, namely, composite carbon fiber, wirewound type, and film-type resistors."*

**EMC characteristics by type:**

| Type | EMC Performance | Application |
|------|-----------------|-------------|
| **Wirewound** | Low noise, high power | High-power applications |
| **Film chip** | Low parasitic inductance | RF and high-speed circuits |
| **Composite carbon** | Higher noise | General purpose |

**Key EMC considerations for resistors:**
- Terminal inductance affects RF performance
- Film chip resistors have better high-frequency characteristics
- Wirewound resistors have higher series resistance at high frequencies

### 7.1.2 Capacitors | 电容器

**From the source:** *"Capacitors are used for decoupling, filtering, and bypass applications. The selection depends on the frequency range and capacitance requirements."*

**Types and EMC characteristics:**

| Type | Frequency Range | EMC Notes |
|------|-----------------|-----------|
| **Ceramic (MLCC)** | High frequency | Good for decoupling, low ESR |
| **Electrolytic** | Low frequency | Large capacitance, higher ESL |
| **Film** | Wide frequency | Low losses, stable |
| **Tantalum** | Medium frequency | Good for filtering, watch polarity |

**Decoupling application from source:**
> *"Decoupling capacitors should be placed close to the power pins of ICs to provide a low-impedance path for high-frequency current demands."*

### 7.1.3 Inductors | 电感器

**From the source:** *"Inductors are used in power supply filters and signal circuits. The self-resonant frequency is a key parameter for EMC design."*

**Key parameters:**
- **L (inductance):** Henry [H]
- **SRF (self-resonant frequency):** $f_{sr} = \frac{1}{2\pi\sqrt{LC}}$
- **DCR (DC resistance):** Affects losses and Q factor

### 7.1.4 Semiconductor Discrete Components | 半导体分立器件

**From the source:** *"Semiconductor devices include diodes, transistors, and MOSFETs. Their switching characteristics generate electromagnetic emissions."*

**EMC considerations:**
- **Switching speed:** Faster transitions generate more emissions
- **Body diode recovery:** Causes voltage overshoots
- **Parasitic capacitance:** Affects high-frequency behavior

### 7.1.5 Transformer | 变压器

**Key EMC issues from source:**
- Magnetic flux leakage causing radiated emissions
- Inter-winding capacitance causing capacitive coupling
- Core saturation causing distortion

### 7.1.6 Digital Circuit Devices | 数字电路器件

**From the source:** *"Digital circuits generate broadband emissions due to fast clock edges and transient switching currents."*

**Key parameters affecting EMC:**
| Parameter | Impact | Mitigation |
|-----------|--------|-----------|
| Clock frequency | Fundamental emission frequency | Use lowest adequate frequency |
| Edge rate (rise/fall time) | High-frequency content | Use slowest acceptable edge rate |
| Output drive strength | Peak current, emission level | Use minimum adequate drive |
| I/O architecture | Simultaneous switching noise | Spread transitions, proper termination |

---

## 7.2 Functions, Components, and Features of Power Supply | 电源的功能、组成与特点

**From the source:** *"Power supply systems in spacecraft must provide clean, stable power while meeting EMC requirements for conducted emissions and susceptibility."*

**Power supply architecture:**
- Primary power: Main bus (e.g., 28 V, 100 V)
- Secondary power: Regulated voltages (5 V, 3.3 V, etc.)
- Payload power: Dedicated, isolated supplies

**EMC requirements for power supplies:**
- Low conducted emission (CE101, CE102 compliance)
- High input immunity (CS101, CS114 compliance)
- Isolation between power domains

---

## 7.3 EMC Design for Power Distribution Unit | 配电单元的EMC设计

**From the source:** *"Power distribution units (PDU) route power from the primary bus to various spacecraft loads while maintaining EMC integrity."*

**Key design considerations:**
1. **Input filtering:** Reduce conducted emissions from upstream
2. **Output filtering:** Isolate load switching noise from bus
3. **Shielding:** Contain magnetic field radiation from transformers/inductors
4. **Grounding:** Single-point ground for control circuits

---

## 7.4 EMC Design of the DC/DC Converter Module | DC/DC转换器模块的EMC设计

### 7.4.1 EMI Interference Analysis | EMI干扰分析

**From the source:** *"DC/DC converters generate EMI through their switching action. The main noise sources are the power switch, transformer, and output rectifier."*

**Switching noise spectrum:**
$$V_{\text{noise}}(f) \propto V_{\text{switch}} \cdot t_{\text{rise}} \cdot f_{\text{switch}}$$

**Key emission frequencies:**
- Fundamental switching frequency $f_{\text{sw}}$
- Harmonics at $nf_{\text{sw}}$ (n = 2, 3, ...)
- Pulse edge energy at frequencies up to $1/(\pi t_{\text{rise}})$

### 7.4.2 Absorption Circuit Design | 吸收电路设计

**From the source:** *"Snubber circuits (absorption circuits) are used to dampen voltage spikes and ringing caused by the switching transients."*

**Snubber types:**
| Type | Application | Characteristics |
|------|-------------|----------------|
| **RC snubber** | Voltage clamping | Dissipates energy in resistor |
| **RCD snubber** | Diode recovery | Catches diode recovery current |
| **TVS diode** | Transient suppression | Clamps voltage at breakdown |

### 7.4.3 Power Filter Design | 电源滤波器设计

**From the source:** *"Power filters attenuate conducted emissions from the converter while allowing DC current to pass."*

**Filter design parameters:**
| Parameter | Symbol | Typical Range |
|-----------|--------|--------------|
| Cutoff frequency | $f_c$ | 10 kHz - 1 MHz |
| Insertion loss | $IL$ | > 40 dB |
| Differential mode attenuation | $IL_{DM}$ | > 60 dB |
| Common mode attenuation | $IL_{CM}$ | > 40 dB |

**Filter topology:**
```
Line → L (DM) → C (DM) → L (CM) → C (CM) → Load
         ↑         ↑
       Common mode chokes
```

---

## 7.5 EMC Design for the Data Acquisition Unit | 数据采集单元的EMC设计

### 7.5.1 Selection of Appropriate Components | 适当元器件的选择

**From the source:** *"Data acquisition units sample analog signals and convert them to digital format. The ADC resolution, sampling rate, and input conditioning all affect EMC performance."*

**Key EMC considerations:**
- ADC clock jitter affects spectral purity
- Input filtering prevents aliasing and reduces emissions
- Proper shielding of analog front-end

---

**Note:** This notes is based on Chapter 7 of Zhang, *Spacecraft Electromagnetic Compatibility Technologies* (2020), pp. 212-250. Bilingual format, content from original source.
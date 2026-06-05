#!/usr/bin/env python3
"""
Balanis Antenna Theory - Bilingual (EN/CN) structure fixer.
COMPLETELY REWRITES the ## section structure from scratch.
Logic:
  - Scan all ## lines; classify each as EN or CN-only
  - For each EN line in SECTION_CN: generate EN + CN pair
  - For each EN line NOT in SECTION_CN: keep EN only
  - ALL CN-only lines: skip entirely (stale duplicates from previous runs)
  - Rebuild the file preserving all content lines exactly
  - Result: idempotent — running again produces the same output
"""

import re
import os

NOTES_DIR = "/home/ubuntu/.openclaw/workspace/textbooks/balanis/notes"

CHAPTER_TITLES = {
    "01": ("Introduction", "引言"),
    "02": ("Fundamental Parameters of Antennas", "天线基础参数"),
    "03": ("Radiation Integrals and Auxiliary Potential Functions", "辐射积分与辅助势函数"),
    "04": ("Linear Wire Antennas", "线天线"),
    "05": ("Loop Antennas", "环形天线"),
    "06": ("Array Antennas", "天线阵"),
    "07": ("Antenna Synthesis", "天线综合"),
    "08": ("Integral Equations, Moment Method, and Self and Mutual Impedances", "积分方程、矩量法与自阻抗/互阻抗"),
    "09": ("Broadband Dipoles and Matching Techniques", "宽带偶极子与匹配技术"),
    "10": ("Traveling Wave and Broadband Antennas", "行波天线与宽带天线"),
    "11": ("Frequency-Independent Antennas", "频率无关天线"),
    "12": ("Aperture Antennas", "口径天线"),
    "13": ("Horn Antennas", "喇叭天线"),
    "14": ("Microstrip Antennas", "微带天线"),
    "15": ("Reflector Antennas", "反射面天线"),
    "16": ("Smart Antennas", "智能天线"),
    "17": ("Antenna Measurements", "天线测量"),
}

SECTION_CN = {
    "Types of Antennas": "天线分类",
    "Radiation Mechanism": "辐射机理",
    "Frequency Bands": "频段划分",
    "Computational Electromagnetics in Antenna Design": "计算电磁学在天线设计中的应用",
    "Fundamental Parameters": "基础参数",
    "Radiation Pattern": "辐射方向图",
    "Beamwidth": "波束宽度",
    "Directivity": "方向性系数",
    "Gain": "增益",
    "Antenna Efficiency": "天线效率",
    "Input Impedance": "输入阻抗",
    "Bandwidth": "带宽",
    "Polarization": "极化",
    "Antenna Noise Temperature": "天线噪声温度",
    "Maxwell's Equations Review": "麦克斯韦方程组回顾",
    "Vector Potential Functions": "矢量势函数",
    "Solution of the Inhomogeneous Helmholtz Equation": "非齐次Helmholtz方程的解",
    "Radiation Integrals": "辐射积分",
    "Far-Field Approximations": "远场近似",
    "Infinitesimal Dipole": "无穷小偶极子",
    "Finite-Length Dipole": "有限长度偶极子",
    "Half-Wavelength Dipole": "半波长偶极子",
    "Linear Elements Near Ground": "地面附近的线天线",
    "Folded Dipole": "折合偶极子",
    "Yagi-Uda Antenna": "八木宇田天线",
    "Log-Periodic Dipole Array": "对数周期偶极子阵",
    "Small Circular Loop": "小圆形环",
    "Circular Loop of Constant Current": "恒流圆形环",
    "Circular Loop with Non-Uniform Current": "非均匀电流圆形环",
    "Quality Factor, Bandwidth, and Efficiency": "品质因子、带宽与效率",
    "Far-Field Patterns": "远场方向图",
    "Ground Plane Effects": "地面效应",
    "Mobile Antenna Applications": "移动天线应用",
    "Two-Element Array": "二元阵",
    "N-Element Linear Array": "N元线阵",
    "Broadside Array": "边射阵",
    "Endfire Array": "端射阵",
    "Pattern Multiplication": "方向图乘法原理",
    "Planar Array": "平面阵",
    "Beam Steering": "波束扫描",
    "Grating Lobes": "栅瓣",
    "Schelkunoff's Method": "Schelkunoff方法",
    "Fourier Transform Method": "傅里叶变换法",
    "Woodward-Leeson Method": "Woodward-Leeson法",
    "Taylor Synthesis": "Taylor综合法",
    "From Differential to Integral Equations": "从微分方程到积分方程",
    "Electric Field Integral Equation (EFIE)": "电场积分方程（EFIE）",
    "Magnetic Field Integral Equation (MFIE)": "磁场积分方程（MFIE）",
    "Method of Moments": "矩量法",
    "Thin Wire Approximation": "细线近似",
    "Self Impedance": "自阻抗",
    "Mutual Impedance": "互阻抗",
    "Lossy Wires": "有损导线",
    "Biconical Antenna": "双锥天线",
    "Triangular Sheet, Bow-Tie, and Wire Simulation": "三角形金属片、Bow-Tie及导线模拟",
    "Cylindrical Dipole": "圆柱偶极子",
    "Matching Techniques for Dipole Antennas": "偶极子天线匹配技术",
    "Discone and Conical Skirt Monopoles": "Discone与锥形单极子",
    "Self-Complementary Antennas": "自互补天线",
    "Broadband Characteristics of Some Other Antennas": "其他天线的宽带特性",
    "Traveling Wave Antennas": "行波天线",
    "Long Wire": "长导线",
    "V-Antenna": "V形天线",
    "Rhombic Antenna": "菱形天线",
    "Broadband Antennas": "宽带天线",
    "Helical Antenna": "螺旋天线",
    "Rumsey's Principle": "Rumsey原理",
    "Log-Periodic Antennas": "对数周期天线",
    "Spiral Antennas": "螺旋天线",
    "Aperture Theory": "口径理论",
    "Huygens' Principle": "Huygens原理",
    "Babinet's Principle": "Babinet原理",
    "Waveguide Slot Antennas": "波导缝隙天线",
    "Parabolic Reflector Antennas": "抛物面反射器天线",
    "Pyramidal Horn": "角锥喇叭",
    "Conical Horn": "圆锥喇叭",
    "Corrugated Horn": "波纹喇叭",
    "Aperture-Matched Horns": "口径匹配喇叭",
    "Potter's Horn": "Potter喇叭",
    "Microstrip Antennas": "微带天线",
    "Transmission-Line Model": "传输线模型",
    "Cavity Model": "腔体模型",
    "Rectangular Patch": "矩形贴片",
    "Circular Patch": "圆形贴片",
    "Feed Techniques": "馈电技术",
    "Array Configuration": "阵列配置",
    "Reflector Antennas": "反射面天线",
    "Parabolic Reflector": "抛物面反射器",
    "Cassegrain Reflector": "卡塞格伦反射器",
    "Shrouded Reflectors": "遮罩反射器",
    "Polarization Characteristics": "极化特性",
    "Smart Antenna System Architecture": "智能天线系统架构",
    "Direction of Arrival Estimation": "到达方向估计",
    "Adaptive Beamforming": "自适应波束形成",
    "Space Division Multiple Access": "空分多址",
    "Antenna Ranges": "天线测试场",
    "Reflection Range": "反射测试场",
    "Free-Space Range": "自由空间测试场",
    "Compact Range": "紧缩场",
    "Impedance Measurement": "阻抗测量",
    "Pattern Measurement": "方向图测量",
    "Gain Measurement": "增益测量",
    "Polarization Measurement": "极化测量",
    "Anechoic Chamber": "电波暗室",
}

HAS_CN_RE = re.compile(r'[\u4e00-\u9fff]')

def has_chinese(text):
    return bool(HAS_CN_RE.search(text))

def extract_en_key(h2_line):
    m = re.match(r'^(##\s+)([\d\.]+\s+)?(.*)', h2_line)
    if not m:
        return None
    raw = m.group(3).strip()
    t = re.sub(r'\s*[\uff08-\uff09(（#【].*', '', raw).strip()
    return re.sub(r'^[\d\.]+\s+', '', t)

def chapter_num_from_filename(fname):
    m = re.search(r'ch(\d+)', fname)
    return m.group(1).zfill(2) if m else None

def is_stale_cn_heading(line):
    """Return True if this is a CN-only heading (stale, to be removed)."""
    if not has_chinese(line):
        return False
    h2 = re.match(r'^(##\s+)([\d\.]+\s+)?(.*)', line)
    if not h2:
        return False
    en_key = extract_en_key(line)
    # Stale if: it's a CN heading but its EN key is NOT in SECTION_CN
    # (meaning it was auto-added CN that we should regenerate, or an untranslated CN section)
    if en_key and en_key not in SECTION_CN:
        return True
    return False

def process_file(filepath):
    with open(filepath, encoding='utf-8') as f:
        raw = f.read()

    fname = os.path.basename(filepath)
    ch_num = chapter_num_from_filename(fname)
    lines = raw.split('\n')
    n = len(lines)

    result = []
    i = 0

    # ── Line 0: chapter heading ──
    if n > 0 and re.match(r'^#\s+Chapter\s+\d+', lines[0]):
        result.append(lines[0])
        if ch_num and ch_num in CHAPTER_TITLES:
            cn = CHAPTER_TITLES[ch_num][1]
            if n > 1 and re.match(r'^#\s+第', lines[1]):
                result.append(lines[1])
            else:
                result.append(f"# 第{int(ch_num):d}章：{cn}")
        else:
            if n > 1:
                result.append(lines[1])
        i = 2
    elif n > 0 and re.match(r'^#\s+Balanis\s+Ch\d+', lines[0]):
        m = re.match(r'^#\s+Balanis\s+Ch(\d+):\s*(.*)', lines[0])
        if m:
            cnum = m.group(1).zfill(2)
            rest = m.group(2).strip()
            if cnum in CHAPTER_TITLES:
                en_full = f"Chapter {int(cnum)}: {CHAPTER_TITLES[cnum][0]}"
                cn = CHAPTER_TITLES[cnum][1]
            else:
                en_full = f"Chapter {int(cnum)}: {rest}"
                cn = rest
            result.append(f"# {en_full}")
            if n > 1 and re.match(r'^#\s+第', lines[1]):
                result.append(lines[1])
            else:
                result.append(f"# 第{int(cnum):d}章：{cn}")
        i = 2
    else:
        i = 0

    # ── Stream through lines ──
    while i < n:
        line = lines[i]
        h2 = re.match(r'^(##\s+)([\d\.]+\s+)?(.*)', line)

        if not h2:
            result.append(line)
            i += 1
            continue

        # This is a ## heading
        en_key = extract_en_key(line)

        if has_chinese(line):
            # CN-only heading: skip (stale)
            i += 1
            continue

        # EN-only heading: emit it + optional CN subtitle
        result.append(line)
        if en_key and en_key in SECTION_CN:
            m = re.match(r'^(##\s+)', line)
            prefix = m.group(1) if m else "## "
            result.append(f"{prefix}{SECTION_CN[en_key]}")

        i += 1

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('\n'.join(result))

    print(f"Fixed: {fname}")

def main():
    files = sorted([f for f in os.listdir(NOTES_DIR) if f.endswith('.md')])
    print(f"Found {len(files)} .md files")
    for fname in files:
        process_file(os.path.join(NOTES_DIR, fname))
    print(f"\nDONE: Balanis 双语修正完成，{len(files)} 个文件")

if __name__ == '__main__':
    main()

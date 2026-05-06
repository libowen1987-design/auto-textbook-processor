# 🔬 Auto-Textbook-Processor & Electromagnetism Notes

> **29本电磁学经典教材的 Python 复现 · 700+ 张科学图表 · 300+ 份可运行代码**

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/yourusername/auto-textbook-processor.svg?style=social)](https://github.com/yourusername/auto-textbook-processor/stargazers)

---

## ⚠️ 免责声明（重要）

> **本项目不包含任何受版权保护的原版 PDF 或电子书文件。**
>
> 所有内容均为个人学习笔记、基于物理定律的原创 Python 仿真代码、以及从公开公式推导生成的科学图表，属于合理使用（Fair Use）。
>
> 本项目仅包含个人对基本电磁学理论的理解与代码实现，不对任何教材内容主张版权。如需原书请通过正规渠道**购买支持正版**。

---

## 📖 项目简介

本项目是本人历时多年积累的**电磁场与微波技术**学习资源库，包含：

- 📚 **29本电磁学经典教材**的系统性学习笔记（Markdown + LaTeX 公式）
- 💻 **300+ 个可运行的 Python 仿真程序**（覆盖传输线、天线、FDTD、FEM、散射等）
- 📊 **700+ 张科学图表**（由代码生成，非扫描件，展示电磁场分布、频响特性、史密斯圆图等）
- ⚡ **OpenClaw 工作流技能**（`textbook-digitizer.skill`）用于自动化教材数字化

### 覆盖的主要教材

| 领域 | 代表书籍 |
|------|---------|
| 电磁场理论 | Griffiths《Introduction to Electrodynamics》, Jackson《Classical Electrodynamics》 |
| 微波工程 | Pozar《Microwave Engineering》, Collin《Foundations for Microwave Engineering》 |
| 天线 | Balanis《Antenna Theory》, Kraus《Antennas》 |
| 计算电磁学 | Taflove《Computational Electrodynamics》, Jin《The Finite Element Method》 |
| 微波技术 | 梁昌洪《简明微波》, 廖承恩《微波技术基础》 |
| 经典电动力学 | Landau《Electrodynamics of Continuous Media》, 郭硕鸿《电动力学》 |

---

## 📂 目录结构

```
auto-textbook-processor/
├── .gitignore                 # 过滤原始PDF等版权材料
├── README.md                  # 本文件
├── LICENSE                    # MIT License
│
├── scripts/                   # Python 仿真代码
│   ├── balanis/              # Balanis 天线论 代码
│   ├── pozar/                # Pozar 微波工程 代码
│   ├── taflove/              # FDTD 时域有限差分 代码
│   ├── sadiku/               # Sadiku 电磁学基础 代码
│   ├── skrf/                 # scikit-rf 微波网络分析
│   └── [其他教材同名文件夹]/
│
├── study_notes/              # 学习笔记（Markdown + LaTeX）
│   ├── balanis/              # 按教材分章节整理
│   ├── pozar/
│   ├── griffiths/
│   └── ...
│
├── assets/                   # 生成的可视化图表
│   └── images/               # 700+ 张 PNG 科学图表
│       ├── balanis/          # 与各教材代码对应
│       ├── fdtd_fields/      # FDTD 场分布可视化
│       ├── smith_charts/     # 史密斯圆图
│       └── [其他]
│
└── openclaw_skills/          # OpenClaw AI 工作流技能
    ├── textbook-digitizer.skill   # 教材数字化完整流水线
    └── references/           # 技能参考文档
        ├── ocr-pipeline.md
        ├── python-templates.md
        └── quality-audit.md
```

### 各目录用途说明

| 目录 | 内容 | 是否原创 |
|------|------|:-------:|
| `scripts/` | Python 仿真代码，基于物理公式编写 | ✅ |
| `study_notes/` | 学习笔记，对应各章节的公式整理与推导 | ✅ |
| `assets/images/` | 代码生成的科学图表（非扫描，非拍照） | ✅ |
| `openclaw_skills/` | AI 工作流定义文件 | ✅ |
| *(无 `pdf/` 目录)* | **本项目不包含任何 PDF** | — |

---

## 🛠️ 快速开始

### 环境依赖

```bash
pip install numpy matplotlib scipy scikit-rf pyfmm pymupdf pdfplumber

# 可选：科学绘图风格
pip install scienceplots
```

### 运行示例

```bash
# 复现 Pozar 微波工程 第4章 阻抗匹配实例
python scripts/pozar/pozarch4_impedance_matching.py

# 生成 Balanis 天线方向图
python scripts/balanis/balanis_ch4_pattern_synthesis.py

# FDTD 电磁场传播可视化
python scripts/taflove/fdtd_2d_tezwave.py
```

### 生成图表

```bash
python scripts/pozar/pozarch4_impedance_matching.py
# 输出: assets/images/pozar_ch4_matching.png
```

---

## 📊 成果统计

| 指标 | 数量 |
|------|:----:|
| 覆盖教材 | **29 本** |
| Python 代码文件 | **300+ 个** |
| 生成图表 | **700+ 张** |
| 覆盖章节 | **314 章节** |
| OpenClaw Skill | **1 个** |

---

## 🤝 支持与打赏

如果这个项目对你的学习或研究有帮助，欢迎通过以下方式支持：

### GitHub Sponsors
[![GitHub Sponsor](https://img.shields.io/badge/GitHub-Sponsor-ea4aaa?style=for-the-badge&logo=github)](https://github.com/sponsors/libowen1987-design)

### Buy Me a Coffee
[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=for-the-badge&logo=buy-me-a-coffee)](https://www.buymeacoffee.com/libowen1987-design)

### 微信 / 支付宝赞赏码
如果本项目对您有帮助，欢迎请作者喝杯咖啡 ☕️

<div align="center">
  <img src="assets/sponsor_wechat_qr.png" width="250" alt="微信赞赏码">
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="assets/sponsor_alipay_qr.png" width="250" alt="支付宝赞赏码">
</div>

---

## 📄 License

本项目采用 [MIT License](LICENSE)。

- ✅ 可以： fork、star、提交 PR、学习参考
- ✅ 可以：基于原创代码进行修改和再发布
- ❌ 禁止：将本项目包含的笔记/代码声称是你原创的教材内容
- ❌ 禁止：使用本项目名义分发未经授权的教材 PDF

---

## 🙏 致谢

- **教材作者们**：感谢所有电磁学教材作者的卓越工作
- **开源社区**：感谢 `numpy`、`scipy`、`matplotlib`、`scikit-rf` 等项目的维护者
- **OpenClaw**：感谢提供 AI Agent 框架支持

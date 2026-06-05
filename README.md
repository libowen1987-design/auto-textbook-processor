# 🔬 Auto-Textbook-Processor & Electromagnetism Notes

> **27本电磁学经典教材的 Python 复现 · 1,200+ 张科学图表 · 350+ 份可运行代码**

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

- 📚 **27本电磁学经典教材**的系统性学习笔记（Markdown + LaTeX 公式）
- 💻 **350+ 个可运行的 Python 仿真程序**（覆盖传输线、天线、FDTD、FEM、散射等）
- 📊 **1,200+ 张科学图表**（由代码生成，非扫描件，展示电磁场分布、频响特性、史密斯圆图等）
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
├── .gitignore                     # 过滤原始PDF等版权材料
├── README.md                      # 本文件
├── LICENSE                        # MIT License
│
├── openclaw_skills/               # OpenClaw AI 工作流技能
│   ├── SKILL.md                   # 教材数字化流水线定义
│   ├── textbook-digitizer.skill   # 触发器配置
│   └── references/                # OCR/模板/审计参考
│
├── study_notes/                   # 全部27本教材（按书名分目录）
│   └── {book_name}/
│       ├── notes/                 .md 中英双语笔记
│       ├── code/                  .py 例题复现代码
│       └── figures/               .png 科学图表（本地，未推送GitHub）
│
├── assets/                        # 项目资产
│   ├── sponsor_alipay_qr.png      # 支付宝赞赏码
│   └── sponsor_wechat_qr.png      # 微信赞赏码
│
└── [其他文件]
```
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
python study_notes/pozar/code/pozarch04_examples.py

# 生成 Balanis 天线方向图
python study_notes/balanis/code/balanisch06_examples.py

# FDTD 电磁场传播可视化
python study_notes/taflove/code/taflove_fdtd_1d.py
```

### 生成图表

```bash
python study_notes/pozar/code/pozarch04_examples.py
# 输出: study_notes/pozar/figures/ex04_01_series_impedance.png
```

---

## 📊 成果统计

| 指标 | 数量 |
|------|:----:|
| 覆盖教材 | **27 本** |
| Python 代码文件 | **350+ 个** |
| 生成图表 | **1,200+ 张** |
| 覆盖章节 | **342 章节**  
| OpenClaw Skill | **1 个** |

---

## 🤝 支持与打赏

如果这个项目对你的学习或研究有帮助，欢迎通过以下方式支持：

### GitHub Sponsors
[![GitHub Sponsor](https://img.shields.io/badge/GitHub-Sponsor-ea4aaa?style=for-the-badge&logo=github)](https://github.com/sponsors/yourusername)

### Buy Me a Coffee
[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=for-the-badge&logo=buy-me-a-coffee)](https://www.buymeacoffee.com/yourusername)

### 微信 / 支付宝赞赏码
> 赞赏码图片放置于此（可选）：
> ![WeChat QR](assets/sponsor_wechat_qr.png)
> ![Alipay QR](assets/sponsor_alipay_qr.png)

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

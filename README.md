# 📚 电磁神教 — 经典教材数字化图书馆

**27本经典电磁学教材的全套数字化学习资源**

> 涵盖微波工程、天线理论、电磁兼容、计算电磁学、RF电路设计、电动力学等核心领域

---

## 📂 项目结构（唯一）

```
auto-textbook-processor/
├── study_notes/          ← 全部教材资源
│   ├── {book}/           ← 27本教材，各自独立
│   │   ├── notes/        .md 中英双语笔记
│   │   ├── code/         .py 例题复现代码
│   │   └── figures/      .png 科学图表（本地）
│   └── ...
├── assets/               ← 项目资产
├── README.md
└── LICENSE
```

> **说明：** 本项目采用 **study_notes/{book}/notes/** 统一架构。原 `scripts/` 目录已合并至各教材的 `code/` 子目录中，消除所有冗余。

## 📖 教材总表（27本）

### 文字版（21本）
Pozar《微波工程》4th · Balanis《天线理论》3rd · Collins《微波基础》2nd · Bogatin《信号完整性》2nd · Bondeson《计算电磁学》 · Cheng《电磁场与波》 · Chew《CEM快速算法》 · Griffiths《电动力学导论》4th · Harrington《时谐电磁场》 · Hemming · Houle《FDTD Python仿真》 · Jackson《经典电动力学》3rd · Jin《计算电磁场》2nd · Ludwig《RF电路设计》2nd · Paul《电磁兼容》2nd · Razavi《RF微电子》2nd · Sadiku《电磁学基础》6th · Sheng《CEM精要》 · Taflove《FDTD计算电动力学》3rd · Tsang《电磁波散射》 · Zhang《航天器电磁兼容》

### 扫描版（6本）
Kraus《天线》2nd · 梁昌洪《简明微波》 · 廖承恩《微波技术基础》 · 谢处方《电磁场与电磁波》4th · Landau《连续介质电动力学》 · 郭硕鸿《电动力学》3rd

## 📊 全库统计
| 指标 | 本地 | 远程(GitHub) |
|:-----|:----:|:------------:|
| 教材数 | 27 | 27 |
| 笔记 (.md) | 369 | 337 |
| 代码 (.py) | 352 | 321 |
| 图表 (.png) | 1,293 | — |
| 中英双语 | 100% | 100% |
| Python 语法 | 0错误 | 0错误 |

## 🔧 技术栈
- 笔记: Markdown + LaTeX (MathJax)
- 代码: Python 3 + NumPy/SciPy/Matplotlib
- 微波工具: scikit-rf
- OCR: Tesseract 5.3 + PyMuPDF

## 📜 许可
MIT License

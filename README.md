# Auto Textbook Processor

**27 classic EM & microwave textbooks — bilingual notes & Python reproduction.**

Covers microwave engineering, antenna theory, EMC, computational electromagnetics, RF circuit design, and electrodynamics.

---

## Structure

```
auto-textbook-processor/
├── openclaw_skills/       Textbook digitization pipeline
│   ├── SKILL.md           Workflow definition (6 phases)
│   ├── references/        OCR, templates, audit guidelines
│   └── textbook-digitizer.skill
├── study_notes/           27 textbooks, each with:
│   ├── {book}/
│   │   ├── notes/         .md bilingual notes (Chinese + English)
│   │   ├── code/          .py example reproduction code
│   │   └── figures/       .png scientific plots (local)
│   └── ...
├── assets/                Project assets
└── README.md
```

> Note: The original `scripts/` directory has been merged into each textbook's `code/` subdirectory to eliminate redundancy.

## Textbook List (27)

### Text-based (21)
Pozar · Balanis · Collins · Bogatin · Bondeson · Cheng · Chew · Griffiths · Harrington · Hemming · Houle · Jackson · Jin · Ludwig · Paul · Razavi · Sadiku · Sheng · Taflove · Tsang · Zhang

### Scanned + OCR (6)
Kraus · 梁昌洪(Liang) · 廖承恩(Liao) · 谢处方(Xie) · Landau · 郭硕鸿(Guo)

## Statistics
| Metric | Local | Remote (GitHub) |
|--------|-------|-----------------|
| Textbooks | 27 | 27 |
| Notes (.md) | 369 | 337 |
| Code (.py) | 352 | 321 |
| Figures (.png) | 1,293 | — |
| Bilingual coverage | 100% | 100% |
| Python syntax errors | 0 | 0 |

## Tech Stack
- Notes: Markdown + LaTeX (MathJax)
- Code: Python 3 + NumPy/SciPy/Matplotlib
- Microwave tools: scikit-rf
- OCR: Tesseract 5.3 + PyMuPDF

## License
MIT

## Assets
- `assets/sponsor_alipay_qr.png` — Alipay QR code
- `assets/sponsor_wechat_qr.png` — WeChat QR code

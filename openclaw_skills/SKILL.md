---
name: textbook-digitizer
description: "End-to-end pipeline for digitizing academic textbooks: (1) Acquire PDF from web or local filesystem, (2) Classify as text-based or scanned and apply appropriate extraction, (3) Clean OCR noise, split into chapter markdown with LaTeX math, (4) Reproduce worked examples as runnable Python with scipy/matplotlib, (5) Generate scientific figures, (6) Quality audit against per-chapter size and formula-closure standards. Triggers: 'digitize this textbook', 'extract notes from PDF', 'reproduce example from book', 'build study materials from PDF', 'OCR and clean scanned book chapter', 'convert textbook to structured notes with code and figures'."
---

# Textbook Digitizer

Digitize a textbook PDF into **structured markdown notes** + **runnable Python code** + **scientific figures**. Six phases. No fabrication — every claim must trace to PDF content.

## Phase 0: Setup

```bash
# Install dependencies (one-time)
pip install pymupdf pdfplumber matplotlib scipy scikit-rf --quiet
# OCR tools
sudo apt install tesseract-ocr poppler-utils  # English
sudo apt install tesseract-ocr-chi-sim         # Chinese
```

**Workspace structure:**
```
textbooks/<book_id>/
├── pdf/           # Original PDF (never modify)
├── raw/           # OCR raw text (scanned PDFs)
├── notes/         # Cleaned chapter notes (.md)
├── chapters/      # Split chapters (alternative layout)
├── code/          # Python scripts (*.py)
└── figures/       # Generated figures (*.png)
```
`book_id` = lowercase with underscores, e.g. `pozarch3`, `sadiku_eoe`, `landau_edcm`.

---

## Phase 1: Acquire PDF

**Priority order:**
1. Local: `textbooks/*/pdf/` or `raw_pdf/`
2. Web: use `browser` or `web_fetch` to locate IEEE Xplore / Springer / Google Scholar links
3. User-provided path

> ⚠️ Only process PDFs the user owns or that are publicly available. Do not scrape pirate repositories.

---

## Phase 2: Classify and Extract

### 2.1 Classify PDF Type
```python
import fitz
doc = fitz.open("book.pdf")
text_pages = sum(1 for i in range(min(10, len(doc))) 
                 if doc[i].get_text().strip())
is_scanned = text_pages < 3
print(f"Scanned: {is_scanned}, Pages: {len(doc)}")
```

### 2.2 Text-based → Extract via PyMuPDF
```python
import fitz
doc = fitz.open("book.pdf")
toc = doc.get_toc()

# Map chapter number → start page
chapters = []
for level, title, page in toc:
    m = re.match(r'^(\d+)\s+(.*)', title.strip())
    if m and level == 1:
        chapters.append((int(m.group(1)), page, m.group(2)))

for i, (ch_num, start, name) in enumerate(chapters):
    end = chapters[i+1][1] if i+1 < len(chapters) else len(doc)+1
    text = "\n".join(doc[p-1].get_text() for p in range(start, min(end, len(doc)+1)))
    # Save to notes/
```

### 2.3 Scanned → OCR
```bash
# Quick OCR test (first 3 pages)
pdftoppm -r 200 -png book.pdf /tmp/page
for f in /tmp/page-0{1,2,3}.png; do tesseract "$f" stdout -l chi_sim+eng 2>/dev/null | head -5; done

# Full batch (see references/ocr-pipeline.md)
pdftoppm -r 300 -png book.pdf /tmp/pages
for p in /tmp/pages*.png; do tesseract "$p" "${p%.png}" -l chi_sim+eng --psm 6; done
cat /tmp/pages*.txt > raw/book_raw.txt
```

### 2.4 OCR Text Cleaning
```python
def clean_ocr(text):
    # 1. Remove inter-letter spacing: "L i x e" → "Lixe"
    text = re.sub(r'(?<=[a-z])\s+(?=[a-z])', '', text)
    # 2. Hyphenated line breaks: "word-\nnext" → "wordnext"
    text = re.sub(r'-\n(\w)', r'\1', text)
    # 3. Control characters
    text = re.sub(r'[\x00-\x08\x0b-\x0c\x0e-\x1f\x7f-\x9f]', '', text)
    # 4. Collapse whitespace
    text = re.sub(r'[ \t]+', ' ', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()
```

---

## Phase 3: Split into Chapters

**Filename format:** `{book_id}_ch{n}_notes.md`

**Chapter header template:**
```markdown
# {Author}《{Title》第{n}章

> **Source:** {Full citation}  
> **Pages:** p.{start}-{end}  
> **Extraction:** ✅ Clean text PDF | ⚠️ OCR-cleaned

---

## {Chapter Title}

[extracted and cleaned content]
```

**Content rules:**
- ✅ Keep: equations (as LaTeX), theorems, definitions, example problem statements, figure captions, page references
- ❌ Remove: page headers/footers, copyright notices, dedication pages, blank pages
- ❌ **Never fabricate** content not present in the source PDF

---

## Phase 4: Reproduce Examples in Python

**Priority:**
1. **Numeric formulas** — compute and plot (impedance, propagation constant, skin depth)
2. **Example problems** — with known inputs/outputs from the book
3. **Figure-generating code** — reproduce key curves (Bode plots, field patterns, Smith charts)
4. Skip: pure prose concepts, proofs requiring symbolic manipulation, proprietary simulation

**Code template:**
```python
#!/usr/bin/env python3
"""
{Book} Ch{n}: {Topic}
Example {X.Y} — {brief description}
Ref: p.{page}
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import c, epsilon_0, mu_0, pi

# Physical constants ONLY from scipy.constants — never hardcode
# Variable names must reflect physics: Z_0, epsilon_r, alpha_dB, VSWR, gamma, beta
# Bad: a, x, val1  Good: Z_0, f_GHz, epsilon_r

# ... reproduce the example ...

# Scientific figure output
plt.style.use('science')
plt.savefig('figures/book_ch{n}_example.png', dpi=150, bbox_inches='tight')
```

**Physics variable naming (electromagnetics):**
| Quantity | Variable | Unit |
|----------|----------|------|
| Characteristic impedance | `Z_0` | Ω |
| Relative permittivity | `epsilon_r` | — |
| Propagation constant | `gamma` | rad/m |
| Attenuation constant | `alpha` | Np/m |
| Phase constant | `beta` | rad/m |
| Reflection coefficient | `Gamma` | complex |
| VSWR | `VSWR` | — |
| Skin depth | `delta_s` | m |
| Wavelength | `lambda_` | m |

---

## Phase 5: Quality Audit

Run after each chapter:

| Check | Threshold | If Fail |
|-------|-----------|---------|
| Per-chapter size | ≥5 KB (A-grade ≥15 KB) | Expand or investigate |
| LaTeX balance | Every `$` and `$$` closed | Fix regex errors |
| Python runs | `python3 code.py` exits 0 | Debug before continuing |
| Figure exists | ≥1 per chapter | Generate representative plot |
| Source cited | Header has author/title/pages | Add provenance block |

**Quality grades:**
- 🟢 **A**: ≥15 KB/chapter, code+figures, PDF-sourced
- 🟡 **B**: 5–15 KB, code or figures present
- 🟠 **C**: 5–15 KB, code or figures sparse
- 🔴 **D**: <5 KB/chapter — review: is content thin or just not extracted?

---

## Phase 6: Archive

```bash
# Copy to canonical library
cp -r textbooks/<book_id>/ /opt/maxwell/leader_workspace/canonical_library/
```

---

## Quick Reference

| Need | Tool | Command |
|------|------|---------|
| PDF text extraction | `fitz` (PyMuPDF) | `doc.get_text()`, `doc.get_toc()` |
| PDF→images for OCR | `pdftoppm` | `pdftoppm -r 300 -png file.pdf prefix` |
| OCR | `tesseract` | `tesseract img.png out -l chi_sim+eng` |
| PDF OCR in-place | `ocrmypdf` | `ocrmypdf --sidecar out.txt in.pdf out.pdf` |
| Physical constants | `scipy.constants` | `c`, `epsilon_0`, `mu_0`, `pi` |
| Microwave/S-parameters | `skrf` | `rf.Network(s=S, frequency=freq)` |
| Scientific plots | `matplotlib` | `plt.style.use('science')` |

**Detailed references:**
- OCR tools, language packs, PSM modes → [references/ocr-pipeline.md](references/ocr-pipeline.md)
- Python code templates, physics variable names, plot styles → [references/python-templates.md](references/python-templates.md)
- Quality grading rubric and failure recovery → [references/quality-audit.md](references/quality-audit.md)
# Quality Audit Reference

## Per-Checkpoint Thresholds

| Check | Minimum | Target | Method |
|-------|---------|--------|--------|
| Chapter size | 5 KB | 15 KB+ | `wc -c *.md` |
| LaTeX balance | $...$ and $$...$$ both closed | No orphaned `$` | `grep -c '$' ch*.md` |
| Python runability | Exit 0 | All examples pass | `python3 code.py` |
| Figure count | 1 per chapter | 2–5 per chapter | `ls figures/*.png | wc -l` |
| Source header | Present | Has author, title, page range | `head -5 *.md` |

## Quality Grading Rubric

```
🟢 A (Excellent):     ≥15 KB/chapter, code present, ≥2 figures, PDF-sourced
🟡 B (Good):          5–15 KB, code or figures, PDF-sourced
🟠 C (Acceptable):    5–15 KB, sparse code/figures
🔴 D (Needs Work):    <5 KB/chapter — investigate: thin content or extraction failure?
```

## Failure Recovery

### Symptom: `grep -c '$' ch*.md` shows orphaned `$`

**Fix:** Use regex to find unpaired dollars:
```python
import re
text = open('ch.md').read()
dollars = [i for i, c in enumerate(text) if c == '$']
# Odd count = unpaired
if len(dollars) % 2 != 0:
    # Find nearest pair and insert missing $
```

### Symptom: Chapter <5 KB but PDF has content

**Possible causes:**
1. ToC page numbers are wrong → manually find page range by searching PDF
2. PDF has image-based ToC (no text) → use `doc.get_pixmap()` + OCR on ToC pages
3. Chapter is genuinely short (some appendices) → accept as-is

### Symptom: Python exits non-zero

1. Check for undefined variables (run `python3 -c "import py_compile; py_compile.compile('code.py')"`)
2. Verify all `from scipy.constants import ...` imports exist
3. For matplotlib warnings, add `plt.switch_backend('Agg')` before import in scripts

### Symptom: OCR quality is poor (many garbled characters)

**Mitigation:**
- Re-OCR at higher DPI (400–600 dpi instead of 300)
- Try `--psm 4` (single column) vs `--psm 6` (single block)
- For mixed-language: ensure `chi_sim+eng` language pack is installed
- Post-clean with targeted regex based on error patterns

## Automated Audit Script

```python
#!/usr/bin/env python3
"""
audit_chapters.py — batch quality check for all chapters
"""
import os, re, subprocess, sys

def audit_chapter(md_path):
    issues = []
    size_kb = os.path.getsize(md_path) / 1024
    
    with open(md_path) as f:
        text = f.read()
    
    # Size check
    if size_kb < 5:
        issues.append(f"⚠️  Size {size_kb:.1f}KB < 5KB threshold")
    
    # LaTeX balance
    dollars = text.count('$') - text.count(r'\$')
    if dollars % 2 != 0:
        issues.append(f"⚠️  Orphaned $ in LaTeX (count={dollars})")
    
    # Source header
    if not re.search(r'Source:|来源:', text[:500]):
        issues.append("⚠️  No source attribution in header")
    
    return issues

def audit_code(py_path):
    issues = []
    result = subprocess.run(['python3', '-m', 'py_compile', py_path], 
                           capture_output=True, text=True)
    if result.returncode != 0:
        issues.append(f"⚠️  Python syntax error: {result.stderr[:100]}")
    return issues

# Run on all chapters
notes_dir = 'textbooks/book_id/notes'
for fn in sorted(os.listdir(notes_dir)):
    if fn.endswith('.md'):
        path = os.path.join(notes_dir, fn)
        issues = audit_chapter(path)
        if issues:
            print(f"{fn}: " + " | ".join(issues))
        else:
            print(f"✅ {fn}")
```
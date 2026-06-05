# OCR Pipeline Reference

## PDF类型判断

```python
import fitz

def is_scanned_pdf(pdf_path, sample_pages=5):
    """判断PDF是否为扫描件（纯图像，无可提取文字）"""
    doc = fitz.open(pdf_path)
    for i in range(min(sample_pages, len(doc))):
        txt = doc[i].get_text().strip()
        if txt and len(txt) > 50:
            return False  # 有可提取文字
    return True  # 扫描件
```

## OCR工具选择

| 情况 | 推荐工具 | 参数 |
|------|---------|------|
| 中文扫描PDF | tesseract | `tesseract img.png out -l chi_sim+eng` |
| 英文扫描PDF | tesseract | `tesseract img.png out -l eng` |
| PDF原地OCR | ocrmypdf | `ocrmypdf --sidecar out.txt input.pdf out.pdf` |
| 批量处理 | 自适应脚本 | 见下方批量脚本 |

## Tesseract 批量OCR

```bash
#!/bin/bash
# batch_ocr.sh - 批量OCR处理扫描PDF
PDF="$1"
OUTPUT_DIR="$2"
BASENAME=$(basename "$PDF" .pdf)

mkdir -p "$OUTPUT_DIR"

# PDF转图像（300 DPI）
pdftoppm -r 300 -png "$PDF" "$OUTPUT_DIR/${BASENAME}_page"

# 逐页OCR
for img in "$OUTPUT_DIR"/${BASENAME}_page*.png; do
    tesseract "$img" "${img%.png}" -l chi_sim+eng --psm 6 2>/dev/null
done

# 合并为单个文本文件
cat "$OUTPUT_DIR"/${BASENAME}_page*.txt > "$OUTPUT_DIR/${BASENAME}_raw.txt"
echo "OCR完成: $OUTPUT_DIR/${BASENAME}_raw.txt"
```

## 自适应OCR脚本（Python）

```python
#!/usr/bin/env python3
"""
ocr_adaptive.py - 根据页面内容自动选择最优OCR策略
"""
import fitz
import subprocess
import re
import os

def ocr_page_image(img_path, lang='chi_sim+eng', psm=6):
    """对单个图像文件执行OCR"""
    cmd = ['tesseract', img_path, img_path.replace('.png', ''), 
           '-l', lang, '--psm', str(psm), 'quiet']
    subprocess.run(cmd, capture_output=True)
    txt_path = img_path.replace('.png', '.txt')
    if os.path.exists(txt_path):
        with open(txt_path, 'r', encoding='utf-8') as f:
            return f.read()
    return ''

def extract_pdf_to_images(pdf_path, output_dir, dpi=300):
    """将PDF页面转换为图像"""
    doc = fitz.open(pdf_path)
    image_paths = []
    for i in range(len(doc)):
        pg = doc[i]
        mat = fitz.Matrix(dpi/72, dpi/72)
        pix = pg.get_pixmap(matrix=mat)
        img_path = os.path.join(output_dir, f'page_{i:04d}.png')
        pix.save(img_path)
        image_paths.append(img_path)
    return image_paths

def clean_ocr_text(text):
    """清洗OCR输出中的常见噪声"""
    # 1. 分离字符聚合（"L i x e" → "Lixe"）
    text = re.sub(r'(?<=[a-z])\s+(?=[a-z])', '', text)
    # 2. 连字符换行（"word-\nnext" → "wordnext"）
    text = re.sub(r'-\n(\w)', r'\1', text)
    # 3. 去除乱码控制字符
    text = re.sub(r'[\x00-\x08\x0b-\x0c\x0e-\x1f\x7f-\x9f]', '', text)
    # 4. 多余空白
    text = re.sub(r'[ \t]+', ' ', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()

# 使用示例
if __name__ == '__main__':
    import sys
    pdf_path, output_dir = sys.argv[1], sys.argv[2]
    os.makedirs(output_dir, exist_ok=True)
    images = extract_pdf_to_images(pdf_path, output_dir, dpi=300)
    all_text = []
    for img in images:
        txt = ocr_page_image(img)
        all_text.append(clean_ocr_text(txt))
    full_text = '\n\n'.join(all_text)
    with open(os.path.join(output_dir, 'combined.txt'), 'w') as f:
        f.write(full_text)
    print(f"OCR完成: {len(images)}页, {len(full_text)}字符")
```

## LaTeX数学公式提取与规范化

```python
import re

def normalize_latex(text):
    """将混杂的公式格式统一为标准LaTeX"""
    # 1. 修复常见TeX拼写错误
    replacements = {
        r'\d+\s*×\s*10\s*\^\s*\{?\s*(-?\d+)\s*\}?': r'×10^\1',  # 科学计数法
        r'\s+times\s+': r'×',
        r'\s+cdot\s+': r'·',
        r'\\nabla \cdot': r'\\nabla\\cdot',
        r'\\nabla \\times': r'\\nabla\\times',
    }
    for pattern, replacement in replacements.items():
        text = re.sub(pattern, replacement, text)
    
    # 2. 确保公式环境闭合
    # 修复未闭合的行内公式
    lines = text.split('\n')
    result = []
    in_math = False
    for line in lines:
        dollar_count = line.count('$') - line.count(r'\$')
        if dollar_count % 2 == 1:
            in_math = not in_math
        result.append(line)
    return '\n'.join(result)

# 3. 矢量符号规范化（电磁学标准）
def normalize_vectors(text):
    """将电磁学矢量统一为加粗格式"""
    # 电场 E → \mathbf{E}
    vector_pairs = [('E', 'E'), ('H', 'H'), ('D', 'D'), ('B', 'B'),
                    ('J', 'J'), ('k', 'k'), ('r', 'r')]
    for vec, _ in vector_pairs:
        # 匹配独立字母变量（前后有空格或边界）
        text = re.sub(rf'(?<![\\a-zA-Z])({vec})(?![a-zA-Z\]])(?=\s|[,\)\.]|$)', 
                      rf'\\mathbf{{{vec}}}', text)
    return text
```

## 多语言OCR语言包

| 语言 | Tesseract参数 | 适用 |
|------|--------------|------|
| 英语 | `-l eng` | 英文教材 |
| 简体中文 | `-l chi_sim` | 中文OCR |
| 混合（英+中）| `-l chi_sim+eng` | 中英文混排 |
| 日语 | `-l jpn` | 日文教材 |
| 俄语 | `-l rus` | 俄文教材 |

## PSM模式（Tesseract页面分割）

| PSM | 描述 | 适用场景 |
|-----|------|---------|
| 3 | Fully automatic page layout | 默认 |
| 4 | Assume single column | 书籍页面 |
| 6 | Assume single uniform block | 单一文本块 |
| 11 | Sparse text only | 稀疏文字 |

推荐书籍使用 `-psm 4`，表格密集页面使用 `-psm 6`。
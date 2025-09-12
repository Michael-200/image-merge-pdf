# Image to PDF Converter 🖼️➡️📄
# Image to PDF Converter 🖼️➡️📄

A simple Python script that converts multiple images into a single PDF file.  
Powered by [Pillow (PIL fork)](https://pillow.readthedocs.io/).

---

## Features
- Supports **JPG, JPEG, PNG, BMP, TIFF, WEBP** (any format supported by Pillow).
- Converts all images in a given folder into one **multi-page PDF**.
- Automatically handles conversion to **RGB** (fixes transparency issues).
- Skips corrupted or unsupported files gracefully.
- Output PDF is created in the order of file names (sorted alphabetically).

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/image-to-pdf.git
   cd image-to-pdf
   ```
2. Install dependencies:
   ```bash
   pip install pillow
   ```

## Usage

Put your images inside a folder (e.g., images/).

Run the script:

```bash
  python convert.py
```
By default, it will create file.pdf in the project folder








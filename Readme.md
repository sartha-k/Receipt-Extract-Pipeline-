# Receipt Extract Pipeline 🧾

A computer vision pipeline that extracts structured data from real-world receipt images.It handles messy, low-quality scans using adaptive preprocessing and deep-learning OCR.

---

## Approach

1. **Preprocessing** — OpenCV adaptive thresholding and noise reduction to handle real-world lighting and shadow issues
2. **OCR** — EasyOCR for deep-learning-based text recognition robust to faded or distorted text
3. **Extraction** — Regex with a "largest price" fallback to ensure data capture even on messy receipts

---

## Tools Used

| Tool | Purpose |
|---|---|
| Python | Core language |
| OpenCV | Image preprocessing |
| EasyOCR | Deep learning OCR |
| Regex | Data cleaning and extraction |

---

## Challenges & Solutions

| Challenge | Solution |
|---|---|
| Lighting & shadows | Adaptive thresholding |
| Noise / faded ink | Denoising + EasyOCR's robust model |
| Missing totals | "Largest price" fallback logic |

---

## Results

- Filtered out numerical noise (IDs, barcodes) using a `$5,000` threshold
- Produced a clean dataset with an **average transaction value of $145.83**

---

## Suggested Improvements

- **LLM integration** — GPT-4o for semantic understanding of itemized lists
- **Web dashboard** — Allow users to manually correct low-confidence extractions
- **GPU acceleration** — CUDA or multiprocessing to reduce batch processing time from ~60 min to under 10 min

---

## How to Run

### 1. Install dependencies

```bash
pip install matplotlib opencv-python easyocr
```

### 2. Add receipt images

Place all `.jpg` / `.png` receipt images inside the `imgs/` folder.

### 3. Run the pipeline

```bash
python main_processor.py
```

This will process all receipts in the `imgs/` folder and output extracted data.

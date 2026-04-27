**Carbon Crunch Assignment**

**Approach**
1: Preprocessing: Used OpenCV for adaptive thresholding and noise reduction to handle real-world lighting issues
2: OCR: Implemented EasyOCR for deep-learning-based text recognition
3: Extraction: Used Regex and fallback logic (largest price detection) to ensure data capture even with messy receipts

**Tools Used**
1: Python
2: OpenCV (Image processing)
3: EasyOCR (Deep Learning OCR)
4: Regex (Data cleaning)

**Challenges**
1: Lighting/Shadows: Solved with Adaptive Thresholding
2: Noise/Faded Ink: Solved with Denoising and EasyOCR's robust model
3: Missing Totals: Solved with a "Largest Price" fallback logic

**Improvements**
1: Suggesting a Large Language Model (LLM) like GPT-4o for better semantic understanding of itemized lists.
2: Adding a Web Dashboard for users to manually correct low-confidence flags
3: In a production environment, I would implement CUDA-enabled GPU acceleration or use multiprocessing to reduce the processing time from ~60 minutes to under 10 minutes.
4: The final pipeline successfully filtered out numerical noise (IDs/Barcodes) by implementing a $5,000 threshold, resulting in a clean dataset with an average transaction value of $145.83

**How to Run**
1: Install all dependencies used in the code(matplotlib, opencv, easyocr)
2: Place images in the imgs folder
3: Run python main_processor.py to run all receipt

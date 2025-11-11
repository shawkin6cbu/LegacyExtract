# pdf_first_page_ocr.py
import os, io, tempfile, fitz              # pip install pymupdf
import numpy as np
from paddleocr import PaddleOCR

PDF = r"C:\Scripts\contract\Abel Contract.pdf"   # ← your file

def pdf_page_to_numpy(pdf_path, dpi=300):
    """Render page 0 to an RGB NumPy array PaddleOCR accepts."""
    page = fitz.open(pdf_path).load_page(0)
    pix  = page.get_pixmap(matrix=fitz.Matrix(dpi/72, dpi/72), alpha=False)
    img  = np.frombuffer(pix.samples, dtype=np.uint8)\
             .reshape(pix.height, pix.width, pix.n)[:, :, :3]      # drop alpha
    return img[:, :, ::-1]     # BGR→RGB :contentReference[oaicite:0]{index=0}

def main():
    ocr = PaddleOCR(
        use_textline_orientation=True,     # new flag – replaces use_angle_cls :contentReference[oaicite:1]{index=1}
        enable_mkldnn=True,                # fastest CPU kernels
        cpu_threads=os.cpu_count()
    )
    img = pdf_page_to_numpy(PDF)
    result = ocr.predict(img)              # accepts ndarray or str only :contentReference[oaicite:2]{index=2}
    for box, (text, score) in result[0]:
        print(f"{text} ({score:.3f})")

if __name__ == "__main__":
    main()
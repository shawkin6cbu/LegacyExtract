# test_ocr.py
from paddleocr import PaddleOCR

# This assumes debug_page_1.png was created in the same folder
# Make sure this path is correct
image_path = "debug_page_1.png" 

# Initialize the OCR engine
ocr = PaddleOCR(lang="en", use_textline_orientation=True)

print("Starting OCR on the saved image...")
result = ocr.predict(image_path)
print("OCR process finished.")

# Print the results
print("\n--- OCR RESULTS ---")
if result and result[0]:
    for line in result[0]:
        print(line[1][0])
else:
    print("No text found in the image.")
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import easyocr

import os


DATA_FILE_PATH = "data"

'''
print("Processing using EasyOCR\n")

reader = easyocr.Reader(["ru"])
for root, dirs, files in os.walk(DATA_FILE_PATH):
    for file in files:
        file_path = os.path.join(root, file)
        if file_path.endswith(".jpg"):
            print(f"Processing file {file_path}")
            result = reader.readtext(file_path)
            print("Result:", result)
            print()
'''

print("\n\nProcessing using Tesseract\n")

for root, dirs, files in os.walk(DATA_FILE_PATH):
    for file in files:
        file_path = os.path.join(root, file)
        if file_path.endswith(".jpg"):
            print(f"Processing file {file_path}")
            custom_config = r'-l eng+jpn --psm 6'
            #result = pytesseract.image_to_string(Image.open(file_path), config=custom_config)
            #result = pytesseract.image_to_boxes(Image.open(file_path), lang="ru")
            result = pytesseract.image_to_data(Image.open(file_path), config=custom_config)
            print("Result:", result)
            print()

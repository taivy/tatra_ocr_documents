try:
    from PIL import Image
except ImportError:
    import Image
import pandas as pd
import pytesseract
import easyocr
from pandas import ExcelWriter


import os


DATA_FILE_PATH = "data"

reader = easyocr.Reader(["ru"])

results = []

for root, dirs, files in os.walk(DATA_FILE_PATH):
    for file in files:
        file_path = os.path.join(root, file)
        if file_path.endswith(".jpg"):
            print(f"Processing file {file_path}")
            #custom_config = r'-l eng+jpn --psm 6'
            #result = pytesseract.image_to_string(Image.open(file_path), config=custom_config)
            result_tesseract = pytesseract.image_to_string(Image.open(file_path), lang="rus")
            #result_tesseract = pytesseract.image_to_data(Image.open(file_path), config=custom_config)
            result_easyocr = "\n".join(reader.readtext(file_path, detail = 0))

            result_dict = {
                "file_path": file,
                "result_tesseract": result_tesseract,
                "result_easyocr": result_easyocr
            }

            results.append(result_dict)

            print("Result:", result_dict)
            print()

df = pd.DataFrame(results)
df.to_excel("ocr_results.xlsx", engine='xlsxwriter')

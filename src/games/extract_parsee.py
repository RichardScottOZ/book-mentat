import os
from pdf_reader import get_elements_from_pdf

input_path = "/mnt/usb_mount/output/Calibre Books"
for root, dirs, files in os.walk(input_path):
    for file in files:
        if '.pdf' in file:
            print(file)
            elements = get_elements_from_pdf("FILE_PATH")
            break

    #break
#If you are processing a PDF that needs OCR but no elements or just very few are being returned, you can force OCR like this (replace the paths):

#elements = get_elements_from_pdf("FILE_PATH", force_ocr=True)
#If you want to visualise the output from the extraction, you can run the following (replace the paths):

#from pdf_reader import visualise_pdf_output
#visualise_pdf_output("FILE_PATH", "OUTPUT_PATH")
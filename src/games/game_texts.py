import os
from pdf_reader import get_elements_from_pdf
#
import pickle

input_path = "/mnt/usb_mount/books/Calibre Library"
output_path = "/mnt/usb_mount/games/parseenumber_test"

if not os.path.exists(output_path):
    os.mkdir(output_path)

for root, dirs, files in os.walk(input_path):
    for file in files:
        print("Processing:", file)
        with open(os.path.join(root,file),'rb') as f:
            elements = pickle.load(f)

        with open(os.path.join(output_path,file + '.txt'),'w') as fo:

            for idx, e in enumerate(elements):

                fo.writelines(e.paragraphs)
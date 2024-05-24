import os
from pdf_reader import get_elements_from_pdf
#
import pickle

input_path = "/mnt/usb_mount/books/Calibre Library"
output_path = "/mnt/usb_mount/games/parseenumber"

file = 'DC Heroes - Rigged Results - Bruce Humphrey.pdf_15225.pkl'

with open(os.path.join(output_path,file),'rb') as f:
    elements = pickle.load(f)

for e in elements:
    print(e)    
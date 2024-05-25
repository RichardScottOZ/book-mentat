
import os
from lithops import FunctionExecutor
from lithops.storage.cloud_proxy import os as cloudos, open as cloudopen
from lithops import Storage

from pdf_reader import get_elements_from_pdf
import pickle
from multiprocessing import Pool

def process_pdf(filepath):
    for root, dirs, files in os.walk(filepath):
        print(filepath)
        for file in files:
            print(file)

if __name__ == "__main__":
    input_path = "books/Calibre Library"
    output_path = "games/parseenumber"

    with FunctionExecutor(runtime='book-mentat-runtime') as fexec:
        filetest = '/books/Calibre Library'
        f = fexec.call_async(process_pdf, filetest)
        print(f.result())

import os
from lithops import FunctionExecutor
from lithops.storage.cloud_proxy import os as cloudos, open as cloudopen
from lithops import Storage

from pdf_reader import get_elements_from_pdf
import pickle
from multiprocessing import Pool

def process_pdf(filepath):
    spdf = Storage()
    flist = spdf.list_objects('lithops-data-books',filepath)
    for f in flist:
        print(f)
if __name__ == "__main__":
    input_path = "books/Calibre Library/"
    output_path = "games/parseenumber"

    with FunctionExecutor(runtime='book-mentat-runtime') as fexec:
        filetest = 'books/Calibre Library/'
        print(filetest)
        f = fexec.call_async(process_pdf, filetest)
        print(f.result())
from lithops import FunctionExecutor
from lithops.storage.cloud_proxy import os, open
from lithops import Storage

from pdf_reader import get_elements_from_pdf
import pickle
from multiprocessing import Pool

def process_pdf(file):
    #import cv2
    from pdf_reader import get_elements_from_pdf
    #output_path = "/mnt/usb_mount/games/parsee"
    output_path = "games/parseenumber"
    
    filelist = file.split('(')
    #print("FILELIST:",filelist)
    filenumber = filelist[-1]
    result = filenumber.index(')')
    filenumber = filenumber[0:result]
    #print("FILENUMBER:",filenumber)

    print("FILE PROCESSING:",file, filenumber)

    newfile = file + '_' + filenumber + '.pkl'

    if os.path.exists( os.path.join(output_path,os.path.basename(newfile)) ):
        print("SKIPPING:",file, filenumber)
        return 

    try:
        elements = get_elements_from_pdf(file)
        #print(elements)
        print("NEWFILE OUTPUT:",output_path,os.path.basename(newfile))
        with open(os.path.join(output_path,os.path.basename(newfile)), 'wb') as f:
            pickle.dump(elements, f)
    except Exception as parseE:
        print(parseE)
        newfile = file + '_' + filenumber + '.error'
        print("ERROR:", file)
        with open(os.path.join(output_path,os.path.basename(newfile)), 'wb') as f:
            pickle.dump(str(parseE), f)

if __name__ == "__main__":
    input_path = "books/Calibre Library"
    output_path = "games/parseenumber"
    filetest = 'Anodyne Printware/Mothership - HULL BREACH VOL. 1 (25633)/Mothership - HULL BREACH VOL. 1 - Anodyne Printware.pdf'
    filetest = 'books/Calibre Library/Sean McCoy/Mothership - WOM-v1.1 (26106)/Mothership - WOM-v1.1 - Sean McCoy.pdf'
    #os.makedirs(output_path, exist_ok=True)
    #counterror = 0

    


    with FunctionExecutor(runtime='book-mentat-runtime') as fexec:

        #lith = lithops.FunctionExecutor(runtime='lithops-ndvi-v312:01')
        #lith.call_async(test, data=())
        #res = lith.get_result()
        #print(res)  # Prints 'hello'        
        f = fexec.call_async(process_pdf, filetest)
        print(f.result())
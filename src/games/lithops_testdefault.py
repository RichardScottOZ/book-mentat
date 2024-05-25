from lithops import FunctionExecutor

import os
from pdf_reader import get_elements_from_pdf
import pickle
from multiprocessing import Pool

def process_pdf(file):
    import pandas as pd
    df = pd.DataFrame()
    df['boring'] = [1]
    print(file)
    return print(df)

input_path = "/mnt/usb_mount/books/Calibre Library"
output_path = "/mnt/usb_mount/games/parseenumber"
filetest = 'Anodyne Printware/Mothership - HULL BREACH VOL. 1 (25633)/Mothership - HULL BREACH VOL. 1 - Anodyne Printware.pdf'
os.makedirs(output_path, exist_ok=True)
#counterror = 0




#with FunctionExecutor(runtime='default-runtime') as fexec:
with FunctionExecutor(runtime='book-mentat-runtime') as fexec:    

    #lith = lithops.FunctionExecutor(runtime='lithops-ndvi-v312:01')
    #lith.call_async(test, data=())
    #res = lith.get_result()
    #print(res)  # Prints 'hello'        
    f = fexec.call_async(process_pdf, filetest)
    print(f.result())
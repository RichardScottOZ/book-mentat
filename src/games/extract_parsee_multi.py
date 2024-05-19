import os
from pdf_reader import get_elements_from_pdf
import pickle
from multiprocessing import Pool

def process_pdf(file):
    from pdf_reader import get_elements_from_pdf
    output_path = "/mnt/usb_mount/games/parsee"
    print("FILE PROCESSING:",file)
    newfile = file + '.pkl'

    try:
        elements = get_elements_from_pdf(file)
        #print(elements)
        print("NEWFILE OUTPUT:",output_path,os.path.basename(newfile))
        with open(os.path.join(output_path,os.path.basename(newfile)), 'wb') as f:
            pickle.dump(elements, f)
    except Exception as parseE:
        print(parseE)
        newfile = file + '.error'
        print("ERROR:", file)
        with open(os.path.join(output_path,os.path.basename(newfile)), 'wb') as f:
            pickle.dump(str(parseE), f)

if __name__ == "__main__":
    input_path = "/mnt/usb_mount/books/Calibre Library"
    output_path = "/mnt/usb_mount/games/parsee"
    os.makedirs(output_path, exist_ok=True)
    counterror = 0

    pool = Pool()  # Create a pool of worker processes
    for root, dirs, files in os.walk(input_path):
        for file in files:
            if file.endswith('.pdf') and not file.endswith('.log'):
                pool.apply_async(process_pdf, args=(os.path.join(root,file),))

    pool.close()  # Close the pool, indicating that no more tasks will be added
    pool.join()  # Wait for all worker processes to complete

    print("FINISHED: and there were ", counterror, " failures")

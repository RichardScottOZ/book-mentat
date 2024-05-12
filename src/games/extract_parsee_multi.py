import os
from pdf_reader import get_elements_from_pdf
import pickle
from multiprocessing import Pool

def process_pdf(file):
    print(file)
    newfile = file + '.pkl'
    try:
        elements = get_elements_from_pdf(os.path.join(root, file))
        with open(os.path.join(output_path, newfile), 'wb') as f:
            pickle.dump(elements, f)
    except Exception as parseE:
        print(parseE)
        newfile = file + '.error'
        print("ERROR:", file)
        with open(os.path.join(output_path, newfile), 'wb') as f:
            pickle.dump('error', f)

if __name__ == "__main__":
    input_path = "/mnt/usb_mount/books/Calibre Library"
    output_path = "/mnt/usb_mount/games/parsee"
    os.makedirs(output_path, exist_ok=True)
    counterror = 0

    pool = Pool()  # Create a pool of worker processes
    for root, dirs, files in os.walk(input_path):
        for file in files:
            if file.endswith('.pdf'):
                pool.apply_async(process_pdf, args=(file,))

    pool.close()  # Close the pool, indicating that no more tasks will be added
    pool.join()  # Wait for all worker processes to complete

    print("FINISHED: and there were ", counterror, " failures")

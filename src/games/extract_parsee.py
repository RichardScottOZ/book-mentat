import os
from pdf_reader import get_elements_from_pdf
#
import pickle

input_path = "/mnt/usb_mount/books/Calibre Library"
output_path = "/mnt/usb_mount/games/parsee"

os.makedirs(output_path, exist_ok=True)
counterror = 0

for root, dirs, files in os.walk(input_path):
    for file in files:
        if '.pdf' in file:
            print(file)
            newfile = file + '.pkl'
            logfile = file + '_main_log.log'
            with open(logfile,'w') as mainlogf:

                try:
                    elements = get_elements_from_pdf(os.path.join(root,file))
                    with open(os.path.join(output_path,newfile),'wb') as f:
                        pickle.dump(elements, f)
                    mainlogf.writelines("COMPLETED: ", str(file))
                except Exception as parseE:
                    print(parseE)
                    newfile = file + '.error'
                    print("ERROR:",file)
                    counterror += 1
                    mainlogf.writelines("ERROR: ", str(file))

                    with open(os.path.join(output_path,newfile),'wb') as f:
                        pickle.dump('error', f)

                    
            #print(elements)
            #break

    #break
print("FINISHED: and there were ",counterror, " failures")    
#If you are processing a PDF that needs OCR but no elements or just very few are being returned, you can force OCR like this (replace the paths):

#elements = get_elements_from_pdf("FILE_PATH", force_ocr=True)
#If you want to visualise the output from the extraction, you can run the following (replace the paths):

#from pdf_reader import visualise_pdf_output
#visualise_pdf_output("FILE_PATH", "OUTPUT_PATH")
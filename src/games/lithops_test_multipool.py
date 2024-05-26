import os
import subprocess
from lithops import FunctionExecutor
from lithops.storage.cloud_proxy import os as cloudos, open as cloudopen
from lithops import Storage

from pdf_reader import get_elements_from_pdf
import pickle
from lithops.multiprocessing import Pool

def process_pdf(file):
    print("FILE BEING PROCESSED:",file)
    from pdf_reader import get_elements_from_pdf
    #output_path = "/mnt/usb_mount/games/parsee"
    output_path = "games/parseenumber"
    #need to find files with parens and handle
    # get number via regex etc. instead

    def list_installed_packages():
        result = subprocess.run(['pip', 'list'], capture_output=True, text=True)
        print(result.stdout)

    #list_installed_packages()

    try:
        filelist = file.split('(')
        filenumber = filelist[-1]
        result = filenumber.index(')')
        filenumber = filenumber[0:result]

        print("FILE PROCESSING:",file, filenumber)
    except Exception as badnumberE:
        print("BADNUMBER:",file)
        return

    newfile = file + '_' + filenumber + '.pkl'

    if cloudos.path.exists( cloudos.path.join(output_path,cloudos.path.basename(newfile)) ):
        print("SKIPPING:",file, filenumber)
        return 

    spdf = Storage()

    file_path = file

    dir_path = os.path.dirname(file_path)
    dir_path = '/tmp/' + dir_path

    os.makedirs(dir_path, exist_ok=True)    

    spdf.download_file('lithops-data-books',file,'/tmp/' + file)

    print(f'File has been written to {file_path}')        
    try:
        elements = get_elements_from_pdf('/tmp/' + file)
        #print(elements)
        print("NEWFILE OUTPUT:",output_path,os.path.basename(newfile))

        dir_path = os.path.dirname('/tmp/' + output_path + '/' + os.path.basename(newfile))
        os.makedirs(dir_path, exist_ok=True)    

        print("TMP PKL:",'/tmp/' + output_path + '/' + os.path.basename(newfile))
        with open('/tmp/' + output_path + '/' + os.path.basename(newfile), 'wb') as f:
            pickle.dump(elements, f)
        print("CREATED PKL:",'/tmp/' + output_path + '/' + os.path.basename(newfile))
        spdf.upload_file('/tmp/' + output_path + '/' + os.path.basename(newfile), 'lithops-data-books', key=output_path + '/' + os.path.basename(newfile))
    except Exception as parseE:
        print(parseE)
        newfile = file + '_' + filenumber + '.error'
        print("ERROR:", file)
        with cloudopen(cloudos.path.join(output_path,cloudos.path.basename(newfile)), 'wb') as f:
            pickle.dump(str(parseE), f)

if __name__ == "__main__":
    input_path = "books/Calibre Library"
    output_path = "games/parseenumber"

    with FunctionExecutor(runtime='book-mentat-runtime') as fexec:
        filepath = 'books/Calibre Library/'
        print("READING:", filepath)
        #f = fexec.call_async(process_pdf, filetest)
        #print(f.result())
        spdfl = Storage()
        flist = spdfl.list_objects('lithops-data-books',filepath)
        plist = []
        for f in flist:
            plist.append(f['Key'])

        print(plist[0:3])

    with Pool() as pool:
        #async_result = pool.map_async(process_pdf, plist[0:3])
        async_result = pool.map_async(process_pdf, plist)
        try:
            result = async_result.get()
            print(result)
        except TimeoutError:
            print("Timed out!")        
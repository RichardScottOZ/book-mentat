import os
import pandas as pd
input_path = "/mnt/usb_mount/books/Calibre Library"
output_path = "/mnt/usb_mount/games/parsee"

counterror = 0

count = -1

with open(os.path.join(input_path,'complete.log'),'w') as f:
    for root, dirs, files in os.walk(input_path):
        for file in files:
            if '.pdf' not in file or '.log' in file:
                continue
            if os.path.exists(os.path.join(output_path,file + '.pkl')):
                print("COMPLETE:", file)
                f.writelines("COMPLETE: " + file + "\n")
            else:
                print("NEED TO CHECK:", file)
                f.writelines("NEED TO CHECK: " + file + "\n")



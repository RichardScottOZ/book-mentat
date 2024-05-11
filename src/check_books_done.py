import pickle
import os
with open('book_dict.pkl','rb') as f:
    book_dict = pickle.load(f)

input_path = "/mnt/usb_mount/output/Calibre Books"
file_list = []
for root, dirs, files in os.walk(input_path):
    for file in files:
        file_list.append(file)

for b in file_list:
    if b in book_dict:
        pass
    else:
        print("STILL NEED:",b)

import os
import subprocess
from lithops import FunctionExecutor
from lithops.storage.cloud_proxy import os as cloudos, open as cloudopen
from lithops import Storage

import pickle

spdf = Storage()

output_path = "games/parseenumber"
input_path = "/mnt/usb_mount/games/parseenumber"

## check cloud and local

with open('/home/richard/localout.txt') as fl:
    l = fl.readlines()

with open('/home/richard/cloudout.txt') as fl:
    c = fl.readlines()

for local in l:
    found = False
    for cloud in c:
        if local in cloud:
            found = True
            break   

    if not found:
        print(local)
        print('lithops-data-books' + output_path + '/' + local.replace(r'\\n','').strip())

        spdf.upload_file(input_path + '/' + local.replace(r'\\n','').strip(), 'lithops-data-books', key=output_path + '/' + local.replace(r'\\n','').strip())

   
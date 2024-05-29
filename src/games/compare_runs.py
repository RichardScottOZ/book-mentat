import os
import subprocess
from lithops import FunctionExecutor
from lithops.storage.cloud_proxy import os as cloudos, open as cloudopen
from lithops import Storage

import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def upload_to_s3(file_name, bucket, object_name=None):
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Initialize a session using Amazon S3
    s3_client = boto3.client('s3')

    try:
        # Upload the file
        s3_client.upload_file(file_name, bucket, object_name)
        print(f"File {file_name} uploaded to {bucket}/{object_name}")
    except FileNotFoundError:
        print(f"The file {file_name} was not found")
    except NoCredentialsError:
        print("Credentials not available")
    except PartialCredentialsError:
        print("Incomplete credentials provided")

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
        
        upload_file = input_path + '/' + local.replace(r'\\n','').strip()
        print(upload_file)
        # Example usage
        upload_to_s3(upload_file, 'lithops-data-books', output_path + '/' + local.replace(r'\\n','').strip())

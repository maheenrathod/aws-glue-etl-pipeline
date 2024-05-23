import boto3
import os

s3 = boto3.client('s3')

def create_s3_folders(bucket_name, folder_names):
    for folder in folder_names:
        if not folder.endswith('/'):
            folder += '/'
    
        s3.put_object(Bucket=bucket_name, Key=folder)

def uplaod_s3_files(bucket_name, file_paths):
    for file_path in file_paths:
        folder_name, file_name = os.path.split(file_path)
        folder_name = folder_name.split('/')[-1] + '/'
        if folder_name not in folder_names:
            print(f"Folder {folder_name} doesn't exist in the S3 bucket.")
            continue

        print(f"Uploading {file_name} to folder {folder_name}")
        s3.upload_file(file_path, bucket_name, f"{folder_name}{file_name}")


bucket_name = "glue-etl-data-lake"
folder_names = ['customers/', 'sales/']
file_paths = ['local-path/customers/customers.csv', 'local-path/sales/sales.csv']

create_s3_folders(bucket_name, folder_names)
uplaod_s3_files(bucket_name, file_paths)
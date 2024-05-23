import boto3

def create_s3_folders(bucket_name, folder_names):
    s3 = boto3.client('s3')

    for folder in folder_names:
        if not folder.endswith('/'):
            folder += '/'
    
        s3.put_object(Bucket=bucket_name, Key=folder)
    
bucket_name = "glue-etl-data-lake"
folder_names = ['customers/', 'sales/']

create_s3_folders(bucket_name, folder_names)
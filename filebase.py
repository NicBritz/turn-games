import boto3
import requests
import json

from botocore.config import Config

s3 = boto3.client('s3')

boto_config = Config(
					region_name = 'us-east-1',
					signature_version = 's3v4')

s3 = boto3.client(
					's3',
					endpoint_url = 'https://s3.filebase.com',
					aws_access_key_id='FilebaseAccess-Key',
					aws_secret_access_key='Filebase-Secret-Key',
					config=boto_config)

bucket = input("Enter your Bucket Name: ")
key= input("Enter your desired object for this upload: ")

print (" Generating pre-signed url...")

response = s3.generate_presigned_url('put_object', Params={'Bucket':bucket,'Key':key}, ExpiresIn=3600, HttpMethod='PUT')

print (response)

if response is None:
		exit(1)

response = requests.put(response)

print('PUT status_code: ', response.status_code)
print('PUT content: ', response.content)rWSkL82k4K2TDk
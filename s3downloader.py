from MapColoniesJSONLogger.logger import generate_logger
import os
import boto3
import json

log = generate_logger('s3-file-downloader', log_level='DEBUG',
                      handlers=[{'type': 'stream', 'output': 'stderr'}, {'type': 'rotating_file', 'path': './logs.log'}])

endpoint_url = os.environ.get('S3_ENDPOINT_URL', 'http://localhost:9000')
aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID', 'minioadmin')
aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY', 'minioadmin')
bucket = os.environ.get('S3_BUCKET', 'mybucket')
use_ssl = os.environ.get('AWS_HTTPS', False)
object_key = os.environ.get('S3_OBJECT_KEY', 'mapproxy.yaml')
destination = os.environ.get('OUTPUT_DESTINATION', f'downloads/{object_key}')

"""
This method download object into local file system.
"""
try:
    if os.path.exists(os.path.dirname(destination)) is False:
        os.makedirs(os.path.dirname(destination))

    resource = boto3.resource('s3', endpoint_url=endpoint_url,
                                aws_access_key_id=aws_access_key_id,
                                aws_secret_access_key=aws_secret_access_key,
                                use_ssl=use_ssl)

    resource.Bucket(bucket).download_file(object_key, destination)
    log.debug(f'Successfully downloaded file to: {destination}')
except Exception as e:
    log.debug(f'Error occurred while trying download file: {e}')

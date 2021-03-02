from MapColoniesJSONLogger.logger import generate_logger
import os
import boto3

endpoint_url = os.environ.get('S3_ENDPOINT_URL', 'http://localhost:9000')
aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID', 'minioadmin')
aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY', 'minioadmin')
bucket = os.environ.get('S3_BUCKET', 'mybucket')
use_ssl = (os.environ.get('AWS_HTTPS', False))
object_key = os.environ.get('S3_OBJECT_KEY', 'mapproxy.yaml')
destination = os.environ.get('OUTPUT_DESTINATION', f'downloads/{object_key}')
log_level = os.environ.get('LOG_LEVEL', 'DEBUG')

log = generate_logger('s3-file-downloader', log_level=log_level,
                      handlers=[{'type': 'stream', 'output': 'stderr'}, {'type': 'rotating_file', 'path': 'logs/logs.log'}])
"""
This method convert string to bool - "True, "Yes", "1" are considered True
"""


def to_bool(string, default):
    # type: (str- bool) -> (bool)

    if string and string.strip():
        return string.strip()[0].lower() in ['1', 't', 'y']
    return default


"""
This method download object into local file system.
"""


try:
    ssl_enabled = to_bool(use_ssl, False)
    if os.path.exists(os.path.dirname(destination)) is False:
        os.makedirs(os.path.dirname(destination))

    resource = boto3.resource('s3', endpoint_url=endpoint_url,
                                aws_access_key_id=aws_access_key_id,
                                aws_secret_access_key=aws_secret_access_key,
                                use_ssl=ssl_enabled)

    resource.Bucket(bucket).download_file(object_key, destination)
    log.debug(f'Successfully downloaded file to: {destination}')
except Exception as e:
    log.error(f'Error occurred while trying download file: {e}')

import sys
import os
import boto3
from src.logger.jsonLogger import Logger

class S3Provider:

    def __init__(self, destination):
        self.endpoint_url = os.environ.get('S3_ENDPOINT_URL', 'http://localhost:9000')
        self.aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID', 'minioadmin')
        self.aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY', 'minioadmin')
        self.bucket = os.environ.get('S3_BUCKET', 'mybucket')
        self.use_ssl = (os.environ.get('AWS_HTTPS', False))
        self.object_key = os.environ.get('S3_OBJECT_KEY', 'mapproxy.yaml')
        self.log_level = os.environ.get('LOG_LEVEL', 'DEBUG')
        self.destination = destination
        self.log = Logger.get_logger_instance()
    
    """
    This method convert string to bool - "True, "Yes", "1" are considered True
    """
    def to_bool(self, string, default):
        # type: (str- bool) -> (bool)

        if string and string.strip():
            return string.strip()[0].lower() in ['1', 't', 'y']
        return default

    """
    This method download object into local file system.
    """
    def getFile(self):
        try:
            self.ssl_enabled = self.to_bool(self.use_ssl, False)
            if os.path.exists(self.destination) == False:
                os.makedirs(self.destination)

            resource = boto3.resource('s3', endpoint_url=self.endpoint_url,
                                        aws_access_key_id=self.aws_access_key_id,
                                        aws_secret_access_key=self.aws_secret_access_key,
                                        use_ssl=self.ssl_enabled)

            resource.Bucket(self.bucket).download_file(self.object_key, f'{self.destination}/{self.object_key}')
            self.log.info(f'Successfully downloaded file to: {self.destination}')
        except Exception as e:
            self.log.error(f'Error occurred while trying download file from S3: {e}')

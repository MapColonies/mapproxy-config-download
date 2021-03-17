from src.enums.providers import Providers
from src.providers.s3Provider import S3Provider
from src.providers.fSProvider import FSProvider
from src.logger.jsonLogger import Logger
import os
import boto3
    
file_provider = os.environ.get('FILE_PROVIDER', 'fs')
source = os.environ.get('SOURCE_FILE', '/source/file/path')
destination = os.environ.get('OUTPUT_DESTINATION', 'downloads')
log = Logger.get_logger_instance()

try:  
    log.info(f'Provider set to {file_provider}')
    if file_provider == Providers.S3.value:
        provider = S3Provider(destination)
        provider.getFile()
    elif file_provider == Providers.FS.value:
        provider = FSProvider(source, destination)
        provider.getFile()
    else:
        raise ValueError('Invalid file provider type, must be "fs" or "s3"')
    
except Exception as e:
    log.error(f'Error occurred: {e}')

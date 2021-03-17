from MapColoniesJSONLogger.logger import generate_logger
import os

class Logger:
    instance = None
    log_level = os.environ.get('LOG_LEVEL', 'DEBUG')
    log_dir = os.environ.get('LOG_DIR', 'logs')

    @classmethod
    def __get_instance(cls):
        if os.path.exists(cls.log_dir) == False:
            os.makedirs(cls.log_dir) 
        return generate_logger(f'mapproxy-config-download', log_level=cls.log_level,
                      handlers=[{'type': 'stream', 'output': 'stderr'}, {'type': 'rotating_file', 'path': f'{cls.log_dir}/logs.log'}])

    @classmethod
    def get_logger_instance(cls):
        if cls.instance is None:
            cls.instance = Logger.__get_instance()
        return Logger.instance
    
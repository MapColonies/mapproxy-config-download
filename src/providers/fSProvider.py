import sys
import os
from shutil import copy
from src.logger.jsonLogger import Logger

class FSProvider:
    def __init__(self, source, destination):
        self.destination = destination
        self.source = source
        self.log = Logger.get_logger_instance()
    
    """
    This method get source file into destination directory.
    """
    def getFile(self):
        try:
            if os.path.exists(self.destination) == False:
                os.makedirs(self.destination)

            copy(self.source, self.destination)   
            self.log.info(f'Successfully copied source file to: {self.destination}')
        except Exception as e:
            self.log.error(f'Error occurred while trying copy source file: {e}')

from singleton_meta import SingletonMeta
from datetime import datetime
class SingletonLogger(metaclass=SingletonMeta):
    _log_file = None

    def __init__(self, path):
        if self._log_file is None:
            self._log_file = open(path, 'w')

    def log(self, record):
        self._log_file.write(f'[{datetime.now()}]-[{record}]')


    def close_log(self):
        self._log_file.close()
        self._log_file = None
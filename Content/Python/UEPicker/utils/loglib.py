import sys
import os
import logging

from typing import Union
import tempfile

def get_log_file():
    logPath = tempfile.gettempdir()
    logPath += "/CTS_temp"
    if not os.path.exists(logPath):
        os.makedirs(logPath)
    logFile = logPath + "/picker_cfg_"
    return logFile


class LogUtil(logging.Logger):
    __FORMATTER = "%(asctime)s — %(name)s — %(levelname)s — %(funcName)s:%(lineno)d — %(message)s"

    def __init__(
            self,
            name: str,
            log_format: str = __FORMATTER,
            level: Union[int, str] = logging.DEBUG
    ) -> None:
        super().__init__(name, level)
        self.formatter = logging.Formatter(log_format)
        self.addHandler(self.__get_stream_handler())

    def __get_stream_handler(self) -> logging.StreamHandler:
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setFormatter(self.formatter)
        return stream_handler

    @staticmethod
    def create(name, log_level: str = 'DEBUG') -> logging.Logger:
        logging.setLoggerClass(LogUtil)
        logger = logging.getLogger(name)

        logger.setLevel(log_level)

        return logger


# TODO: put the code temporarily
import os
import tempfile
import json

import subprocess

# convert .ui -> .py
# pyside6-uic .\Bob.ui -o Bob.py
# pyside6-rcc -o resource_rc.py resource.qrc
#  test
def update_ui_file(ps6_folder):

    uic_path = os.path.join(ps6_folder, "uic.exe")
    base_folder = os.path.dirname(__file__)
    ui_file = os.path.join(base_folder, "Bob.ui")
    py_file = os.path.join(base_folder, "Bob.py")

    # subprocess.call([uic_path, ui_file, "-o", py_file])
    return [uic_path, ui_file, "-o", py_file]
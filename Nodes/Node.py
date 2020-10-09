# -- coding: utf-8 --
from __future__ import unicode_literals
from Arsenal.JenkinsWeb import JenkinsWeb
from Arsenal.ScanDisc import ScanDisk
from Arsenal.Chronicler import log
from celery import Celery
from random import randint
import os


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


class Node(JenkinsWeb):
    def __init__(self, chrono):
        super().__init__()

        self.__version = -1
        self.__delay_from = 1
        self.__delay_to = 59
        self.__delay = 0
        self.__chronometer = chrono

        self._scan_disc = ScanDisk(directory_to_watch=os.path.join(self.DESTINATION, '{}'.format(self)))
        self._scan_disc.run()

    def __set_delay(self):
        self.__delay += randint(self.__delay_from, self.__delay_to)
        if self.__delay > 59:
            self.__delay -= 60
        return self.__delay

    def add_mark(self):
        self.__chronometer.add_marks(whom=self, mark={'Position': self.__set_delay(), 'CallBack': self.check_version})

    def check_version(self):
        self.check_versions()
        self.add_mark()

    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, ver):
        self.__version = ver




# -- coding: utf-8 --
from __future__ import unicode_literals
from Arsenal.Chronicler import log
import shutil
import zipfile
import os


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


# log.info(zip.getinfo('output/node_all_climate.bin'))
# log.info(zip.getinfo('output/node_all_climate.bin').filename)
# log.info(zip.infolist())


class Zip:
    def __init__(self):
        self.zip = None

    def reload(self):
        self.zip = zipfile.ZipFile('/media/qwerty/Back-UP/Firmwares/{}_{}/{}/ZIP/{}.zip'.format(self,
                                                                                                self.data,
                                                                                                self.version,
                                                                                                self.version))
        self.__extract_node()
        self.__extract_A()
        self.__extract_B()
        self.__replace_node()
        self.__replace_A()
        self.__replace_B()
        self.__rmtree()

    def __extract_node(self):
        log.info(self.zip.extract(member='output/node_all_{}.bin'.format(self),
                                  path='/media/qwerty/Back-UP/Firmwares/{}_{}/{}/ZIP/'.format(self, self.data, self.version)))

    def __extract_A(self):
        log.info(self.zip.extract(member='output/{}A.bin'.format(self.version),
                                  path='/media/qwerty/Back-UP/Firmwares/{}_{}/{}/ZIP/'.format(self, self.data, self.version)))

    def __extract_B(self):
        log.info(self.zip.extract(member='output/{}B.bin'.format(self.version),
                                  path='/media/qwerty/Back-UP/Firmwares/{}_{}/{}/ZIP/'.format(self, self.data, self.version)))

    def __replace_node(self):
        log.info(os.replace('/media/qwerty/Back-UP/Firmwares/{}_{}/{}/ZIP/output/node_all_{}.bin'.
                            format(self, self.data, self.version, self),
                            '/media/qwerty/Back-UP/Firmwares/{}_{}/{}/ZIP/node_all_{}.bin'.
                            format(self, self.data, self.version, self)))

    def __replace_A(self):
        log.info(os.replace('/media/qwerty/Back-UP/Firmwares/{}_{}/{}/ZIP/output/{}A.bin'.
                            format(self, self.data, self.version, self.version),
                            '/media/qwerty/Back-UP/Firmwares/{}_{}/{}/ZIP/{}A.bin'.
                            format(self, self.data, self.version, self.version)))

    def __replace_B(self):
        log.info(os.replace('/media/qwerty/Back-UP/Firmwares/{}_{}/{}/ZIP/output/{}B.bin'.
                            format(self, self.data, self.version, self.version),
                            '/media/qwerty/Back-UP/Firmwares/{}_{}/{}/ZIP/{}B.bin'.
                            format(self, self.data, self.version, self.version)))

    def __rmtree(self):
        log.info(shutil.rmtree('/media/qwerty/Back-UP/Firmwares/{}_{}/{}/ZIP/output'.
                               format(self, self.data, self.version)))










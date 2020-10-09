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


# Will be refactoring
class Zip:
    @classmethod
    def zip_reload(cls, name, date, job):
        cls.zip = zipfile.ZipFile('/media/qwerty/Back-UP/Firmwares/{}/{}___{}/ZIP/{}.zip'.format(name, job, date, job))
        cls.__extract_node(name, cls.zip, date, job)
        cls.__extract_A(name, cls.zip, date, job)
        cls.__extract_B(name, cls.zip, date, job)
        cls.__replace_node(name, date, job)
        cls.__replace_A(name, date, job)
        cls.__replace_B(name, date, job)
        cls.__rmtree(name, date, job)

    @staticmethod
    def __extract_node(name, _zip, date, job):
        log.info(_zip.extract(member='output/node_all_{}.bin'.format(name),
                              path='/media/qwerty/Back-UP/Firmwares/{}/{}___{}/ZIP/'.format(name, job, date)))

    @staticmethod
    def __extract_A(name, _zip, date, job):
        log.info(_zip.extract(member='output/{}A.bin'.format(job),
                              path='/media/qwerty/Back-UP/Firmwares/{}/{}___{}/ZIP/'.format(name, job, date)))

    @staticmethod
    def __extract_B(name, _zip, date, job):
        log.info(_zip.extract(member='output/{}B.bin'.format(job),
                              path='/media/qwerty/Back-UP/Firmwares/{}/{}___{}/ZIP/'.format(name, job, date)))

    @staticmethod
    def __replace_node(name, date, job):
        log.info(os.replace('/media/qwerty/Back-UP/Firmwares/{}/{}___{}/ZIP/output/node_all_{}.bin'.
                            format(name, job, date, name),
                            '/media/qwerty/Back-UP/Firmwares/{}/{}___{}/ZIP/node_all_{}.bin'.
                            format(name, job, date, name)))

    @staticmethod
    def __replace_A(name, date, job):
        log.info(os.replace('/media/qwerty/Back-UP/Firmwares/{}/{}___{}/ZIP/output/{}A.bin'.
                            format(name, job, date, job),
                            '/media/qwerty/Back-UP/Firmwares/{}/{}___{}/ZIP/{}A.bin'.
                            format(name, job, date, job)))

    @staticmethod
    def __replace_B(name, date, job):
        log.info(os.replace('/media/qwerty/Back-UP/Firmwares/{}/{}___{}/ZIP/output/{}B.bin'.
                            format(name, job, date, job),
                            '/media/qwerty/Back-UP/Firmwares/{}/{}___{}/ZIP/{}B.bin'.
                            format(name, job, date, job)))

    @staticmethod
    def __rmtree(name, date, job):
        log.info(shutil.rmtree('/media/qwerty/Back-UP/Firmwares/{}/{}___{}/ZIP/output'.
                               format(name, job, date)))









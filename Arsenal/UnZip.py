# -- coding: utf-8 --
from __future__ import unicode_literals
from Arsenal.Chronicler import log
import shutil
import zipfile
import os
import re


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


class Zip:
    def __init__(self, _path):
        self.__zip = zipfile.ZipFile(_path)
        self.__node = _path.split('/')[5]
        self.__job = _path.split('/')[8].split('.zip')[0]
        self.__directory = re.sub('{}.zip'.format(self.__job), '', _path)

    def __enter__(self):
        self.__extract_node()
        self.__extract_a()
        self.__extract_b()
        self.__replace_node()
        self.__replace_a()
        self.__replace_b()
        self.__rmtree()
        
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        ...
        
    def __extract_node(self):
        log.info(self.__zip.extract(member='output/node_all_{}.bin'.format(self.__node),
                                    path=self.__directory))

    def __extract_a(self):
        log.info(self.__zip.extract(member='output/{}A.bin'.format(self.__job),
                                    path=self.__directory))

    def __extract_b(self):
        log.info(self.__zip.extract(member='output/{}B.bin'.format(self.__job),
                                    path=self.__directory))

    def __replace_node(self):
        log.info(os.replace('{}output/node_all_{}.bin'.format(self.__directory, self.__node),
                            '{}node_all_{}.bin'.format(self.__directory, self.__node)))

    def __replace_a(self):
        log.info(os.replace('{}output/{}A.bin'.format(self.__directory, self.__job),
                            '{}{}A.bin'.format(self.__directory, self.__job)))

    def __replace_b(self):
        log.info(os.replace('{}output/{}B.bin'.format(self.__directory, self.__job),
                            '{}{}B.bin'.format(self.__directory, self.__job)))

    def __rmtree(self):
        log.info(shutil.rmtree('{}output'.format(self.__directory)))









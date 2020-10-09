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


# log.info(zip.getinfo('output/node_all_climate.bin'))
# log.info(zip.getinfo('output/node_all_climate.bin').filename)
# log.info(zip.infolist())


# Will be refactoring
class Zip:
    @classmethod
    def zip_reload(cls, _path):
        _node = _path.split('/')[5]
        _job = _path.split('/')[8].split('.zip')[0]
        _directory = re.sub('{}.zip'.format(_job), '', _path)

        cls.zip = zipfile.ZipFile(_path)
        cls.__extract_node(_node=_node, _zip=cls.zip, _directory=_directory)
        cls.__extract_A(_job=_job, _zip=cls.zip, _directory=_directory)
        cls.__extract_B(_job=_job, _zip=cls.zip, _directory=_directory)
        cls.__replace_node(_directory=_directory, _node=_node)
        cls.__replace_A(_directory=_directory, _job=_job)
        cls.__replace_B(_directory=_directory, _job=_job)
        cls.__rmtree(_directory=_directory)

    @staticmethod
    def __extract_node(_node, _zip, _directory):
        log.info(_zip.extract(member='output/node_all_{}.bin'.format(_node),
                              path=_directory))

    @staticmethod
    def __extract_A(_job, _zip, _directory):
        log.info(_zip.extract(member='output/{}A.bin'.format(_job),
                              path=_directory))

    @staticmethod
    def __extract_B(_job, _zip, _directory):
        log.info(_zip.extract(member='output/{}B.bin'.format(_job),
                              path=_directory))

    @staticmethod
    def __replace_node(_directory, _node):
        log.info(os.replace('{}output/node_all_{}.bin'.format(_directory, _node),
                            '{}node_all_{}.bin'.format(_directory, _node)))

    @staticmethod
    def __replace_A(_directory, _job):
        log.info(os.replace('{}output/{}A.bin'.format(_directory, _job),
                            '{}{}A.bin'.format(_directory, _job)))

    @staticmethod
    def __replace_B(_directory, _job):
        log.info(os.replace('{}output/{}B.bin'.format(_directory, _job),
                            '{}{}B.bin'.format(_directory, _job)))

    @staticmethod
    def __rmtree(_directory):
        log.info(shutil.rmtree('{}output'.format(_directory)))









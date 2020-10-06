# -- coding: utf-8 --
from __future__ import unicode_literals
from Arsenal.JenkinsWeb import JenkinsWeb
from Arsenal.Chronicler import log
from Arsenal.UnZip import Zip
from Nodes.Node import Node


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


class Climate(Node, JenkinsWeb, Zip):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return 'climate'


if __name__ == '__main__':
    climate = Climate()
    if climate.check_versions() > climate.version:

        log.info(climate.version)
        climate.version = climate.check_versions()
        log.info(climate.version)

        climate.get_bin()
        climate.get_zip()
        climate.get_deb()

        climate.reload()





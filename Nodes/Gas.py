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


class Gas(Node, JenkinsWeb, Zip):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return 'gas'


if __name__ == '__main__':
    gas = Gas()
    if gas.check_versions() > gas.version:

        log.info(gas.version)
        gas.version = gas.check_versions()
        log.info(gas.version)

        gas.get_bin()
        gas.get_zip()
        gas.get_deb()

        gas.reload()




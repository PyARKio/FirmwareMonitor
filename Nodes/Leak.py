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


class Leak(Node, JenkinsWeb, Zip):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return 'leak'


if __name__ == '__main__':
    leak = Leak()
    if leak.check_versions() > leak.version:

        log.info(leak.version)
        leak.version = leak.check_versions()
        log.info(leak.version)

        leak.get_bin()
        leak.get_zip()
        leak.get_deb()

        leak.reload()




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


class Valve(Node, JenkinsWeb, Zip):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return 'valve'


if __name__ == '__main__':
    valve = Valve()
    if valve.check_versions() > valve.version:

        log.info(valve.version)
        valve.version = valve.check_versions()
        log.info(valve.version)

        valve.get_bin()
        valve.get_zip()
        valve.get_deb()

        valve.reload()




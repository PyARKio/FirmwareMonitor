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


class Door(Node, JenkinsWeb, Zip):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return 'door'


if __name__ == '__main__':
    door = Door()
    if door.check_versions() > door.version:

        log.info(door.version)
        door.version = door.check_versions()
        log.info(door.version)

        door.get_bin()
        door.get_zip()
        door.get_deb()

        door.reload()




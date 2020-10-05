# -- coding: utf-8 --
from __future__ import unicode_literals
from Arsenal.JenkinsWeb import JenkinsWeb
from Arsenal.Chronicler import log
from Nodes.Node import Node
import requests
import bs4


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


class Door(Node, JenkinsWeb):
    def __init__(self):
        super().__init__()
        self.version = None

    def __str__(self):
        return 'door'


if __name__ == '__main__':
    door = Door()
    log.info(door.check_versions())
    door.get_bin()
    door.get_zip()
    door.get_deb()




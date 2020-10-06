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


class Relay(Node, JenkinsWeb, Zip):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return 'relay'


if __name__ == '__main__':
    relay = Relay()
    if relay.check_versions() > relay.version:

        log.info(relay.version)
        relay.version = relay.check_versions()
        log.info(relay.version)

        relay.get_bin()
        relay.get_zip()
        relay.get_deb()

        relay.reload()




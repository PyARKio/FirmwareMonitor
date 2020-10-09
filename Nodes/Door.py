# -- coding: utf-8 --
from __future__ import unicode_literals
from Arsenal.Chronicler import log
from Arsenal.UnZip import Zip
from Nodes.Node import Node


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


class Door(Node):

    def __str__(self):
        return 'door'

    def sc(self):
        self._scan_disc.scan_disc()


if __name__ == '__main__':
    door = Door('')
    if door.check_versions() > door.version:

        log.info(door.version)
        door.version = door.check_versions()
        log.info(door.version)

        door.get_bin()
        door.get_zip()
        door.get_deb()

        Zip.zip_reload(door, door.date, door.job)




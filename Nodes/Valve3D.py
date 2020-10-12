# -- coding: utf-8 --
from __future__ import unicode_literals
from Arsenal.Chronicler import log
from Nodes.Node import Node


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


class Valve3D(Node):

    def __str__(self):
        return 'valve3d'

    def sc(self):
        self._scan_disc.scan_disc()


if __name__ == '__main__':
    valve = Valve3D()
    if valve.check_versions() > valve.version:

        log.info(valve.version)
        valve.version = valve.check_versions()
        log.info(valve.version)

        valve.get_bin()
        valve.get_zip()
        valve.get_deb()





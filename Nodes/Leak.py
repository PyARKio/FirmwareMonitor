# -- coding: utf-8 --
from __future__ import unicode_literals
from Arsenal.Chronicler import log
from Nodes.Node import Node


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


class Leak(Node):

    def __str__(self):
        return 'leak'

    def sc(self):
        self._scan_disc.scan_disc()


if __name__ == '__main__':
    leak = Leak()
    if leak.check_versions() > leak.version:

        log.info(leak.version)
        leak.version = leak.check_versions()
        log.info(leak.version)

        leak.get_bin()
        leak.get_zip()
        leak.get_deb()





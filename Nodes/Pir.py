# -- coding: utf-8 --
from __future__ import unicode_literals
from Arsenal.Chronicler import log
from Nodes.Node import Node


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


class Pir(Node):

    def __str__(self):
        return 'pir'

    def sc(self):
        self._scan_disc.scan_disc()


if __name__ == '__main__':
    pir = Pir()
    if pir.check_versions() > pir.version:

        log.info(pir.version)
        pir.version = pir.check_versions()
        log.info(pir.version)

        pir.get_bin()
        pir.get_zip()
        pir.get_deb()





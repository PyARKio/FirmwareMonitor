# -- coding: utf-8 --
from __future__ import unicode_literals
from Arsenal.Chronicler import log
from Nodes.Node import Node


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


class Plug(Node):

    def __str__(self):
        return 'plug'

    def sc(self):
        self._scan_disc.scan_disc()


if __name__ == '__main__':
    plug = Plug()
    if plug.check_versions() > plug.version:

        log.info(plug.version)
        plug.version = plug.check_versions()
        log.info(plug.version)

        plug.get_bin()
        plug.get_zip()
        plug.get_deb()





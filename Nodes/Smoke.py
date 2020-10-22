# -- coding: utf-8 --
from __future__ import unicode_literals
from Nodes.Node import Node


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


class Smoke(Node):

    def __str__(self):
        return 'smoke'

    def sc(self):
        self._scan_disc.scan_disc()

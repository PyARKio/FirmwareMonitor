# -- coding: utf-8 --
from __future__ import unicode_literals
from Arsenal.Chronicler import log
from Arsenal.UnZip import Zip
from Nodes.Node import Node


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


class Climate(Node):

    def __str__(self):
        return 'climate'

    def sc(self):
        self._scan_disc.scan_disc()


if __name__ == '__main__':
    climate = Climate('')
    if climate.check_versions() > climate.version:

        log.info(climate.version)
        climate.version = climate.job
        log.info(climate.version)

        climate.get_bin()
        climate.get_zip()
        climate.get_deb()

        Zip.zip_reload(climate, climate.date, climate.job)







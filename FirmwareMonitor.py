# -- coding: utf-8 --
from __future__ import unicode_literals
from Arsenal.Chronicler import log
from Arsenal.Chronometer import Chronometer
from Nodes.Climate import Climate
from Nodes.Door import Door
import time


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


class FirmwareMonitor:
    def __init__(self):
        self.__chronometer = Chronometer()
        self.__chronometer.start()

        self.__climate = Climate(chrono=self.__chronometer)
        self.__door = Door(chrono=self.__chronometer)

        self.__climate.add_mark()
        self.__door.add_mark()

    def go(self):
        time.sleep(160)


if __name__ == '__main__':
    fwm = FirmwareMonitor()
    fwm.go()








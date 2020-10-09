# -- coding: utf-8 --
from __future__ import unicode_literals
from Arsenal.Chronicler import log
from Arsenal.Chronometer import Chronometer
from Nodes.Climate import Climate
from Nodes.Door import Door
from Nodes.Gas import Gas
from Nodes.Leak import Leak
from Nodes.Pir import Pir
from Nodes.Plug import Plug
from Nodes.Relay import Relay
from Nodes.Smoke import Smoke
from Nodes.Valve import Valve
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
        self.__gas = Gas(chrono=self.__chronometer)
        self.__leak = Leak(chrono=self.__chronometer)
        self.__pir = Pir(chrono=self.__chronometer)
        self.__plug = Plug(chrono=self.__chronometer)
        self.__relay = Relay(chrono=self.__chronometer)
        self.__smoke = Smoke(chrono=self.__chronometer)
        self.__valve = Valve(chrono=self.__chronometer)

        self.__climate.add_mark()
        self.__door.add_mark()
        self.__gas.add_mark()
        self.__leak.add_mark()
        self.__pir.add_mark()
        self.__plug.add_mark()
        self.__relay.add_mark()
        self.__smoke.add_mark()
        self.__valve.add_mark()

    def go(self):
        while True:
            time.sleep(160)


if __name__ == '__main__':
    fwm = FirmwareMonitor()
    fwm.go()








# -- coding: utf-8 --
from __future__ import unicode_literals
from Arsenal.JenkinsWeb import JenkinsWeb
from Arsenal.Chronicler import log
from Nodes.Node import Node
import requests
import bs4


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


class Climate(Node, JenkinsWeb):
    JOB_CLIMATE = 'job_climate'

    def __init__(self):
        ...

    def get_bin(self):
        ...


if __name__ == '__main__':
    climate = Climate()
    log.info(climate.check_versions(Climate.JOB_CLIMATE))




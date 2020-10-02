# -- coding: utf-8 --
from __future__ import unicode_literals
from abc import ABC, abstractmethod
from Arsenal.Chronicler import log
import requests
import bs4


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


class JenkinsWeb(ABC):
    NODES = 'http://10.8.0.1:9090/view/nodes/'
    DEB = 'http://10.8.0.1:9090/view/nodes/job/climate/ws/rfNode/'
    BIN = 'http://10.8.0.1:9090/view/nodes/job/climate/ws/rfNode/deb/opt/bron/oad-image/climate/'
    ZIP = 'http://10.8.0.1:9090/view/nodes/job/climate/ws/rfNode/build/master/output/'
    ALL = 'http://10.8.0.1:9090/view/nodes/job/climate/ws/rfNode/build/master/output/'

    def __init__(self):
        self.last_error = None

    def check_versions(self):
        try:
            response = requests.get(JenkinsWeb.NODES)
        except Exception as err:
            log.error(err)
            self.last_error = err
            return False

        g = bs4.BeautifulSoup(response.text, 'html.parser')
        job = g.find(id=self).findAll(class_='model-link inside')[1].text

        return job

    def get_bin(self):
        ...


if __name__ == '__main__':
    t = JenkinsWeb()


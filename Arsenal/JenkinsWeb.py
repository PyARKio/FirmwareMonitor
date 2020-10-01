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
    JOB_CLIMATE = 'job_climate'
    JOB_DOOR = 'job_door'
    JOB_GAS = 'job_gas'

    @staticmethod
    def check_versions(job):
        JenkinsWeb.__api_get_method(JenkinsWeb.NODES)
        g = bs4.BeautifulSoup(response.text, 'html.parser')
        job = g.find(id=job).findAll(class_='model-link inside')[1].text

        return job

    @staticmethod
    def get_bin(self):
        ...

    @staticmethod
    def __api_get_method(_url):
        try:
            response = requests.get(_url)
        except Exception as err:
            return {'Response': None, 'Error': err}
        else:
            return {'Response': response, 'Error': None}


if __name__ == '__main__':
    t = JenkinsWeb()


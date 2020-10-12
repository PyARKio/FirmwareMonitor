# -- coding: utf-8 --
from __future__ import unicode_literals
from Arsenal.Chronicler import log
import requests
import bs4
import re
import os


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


class JenkinsWeb:
    DESTINATION = '/media/qwerty/Back-UP/Firmwares/'
    NODES = 'http://10.8.0.1:9090/view/nodes/'
    DEB = 'http://10.8.0.1:9090/view/nodes/job/{}/ws/rfNode/{}'
    BIN = 'http://10.8.0.1:9090/view/nodes/job/{}/ws/rfNode/deb/opt/bron/oad-image/{}/{}'
    ZIP = 'http://10.8.0.1:9090/view/nodes/job/{}/ws/rfNode/build/master/output/*zip*/output.zip'
    DEB_PACK = '{}_1.0_{}_arm64.deb'

    def __init__(self):
        self.__last_error = None
        self.__job = -1
        self.__date = None

    # CHECK AVAILABLE VERSION -------------------------------------------------------------------------
    def check_versions(self):
        try:
            response = requests.get(self.NODES)
        except Exception as err:
            log.error(err)
            self.__last_error = err
            return False

        g = bs4.BeautifulSoup(response.text, 'html.parser')
        if self.__job < int(re.sub('#', '', g.find(id=self.__get_job__str()).findAll(class_='model-link inside')[1].text)):
            self.__job = int(re.sub('#', '', g.find(id=self.__get_job__str()).findAll(class_='model-link inside')[1].text))
            self.__date = re.sub(':', '_', re.sub('-', '_', g.find(id=self.__get_job__str()).findAll('td')[6].get('data')))

            self.get_bin()
            self.get_deb()
            self.get_zip()

        else:
            log.info('ooo')

        # return self.__job

    def __get_job__str(self):
        return 'job_{}'.format(self)

    # DOWNLOAD BIN -------------------------------------------------------------------------------------
    def get_bin(self):
        __bin_A, __bin_B = self.__get_bin_name()
        __get_A, __get_B = self.__get_bin_url(A=__bin_A, B=__bin_B)
        __dest = self.__mkpath_bin()

        try:
            response = requests.get(__get_A)
        except Exception as err:
            log.error(err)
            self.__last_error = err
            return False
        open('{}/{}'.format(__dest, __bin_A), 'wb').write(response.content)

        try:
            response = requests.get(__get_B)
        except Exception as err:
            log.error(err)
            self.__last_error = err
            return False
        open('{}/{}'.format(__dest, __bin_B), 'wb').write(response.content)

    def __get_bin_name(self):
        return '{}A.bin'.format(self.__job), '{}B.bin'.format(self.__job)

    def __get_bin_url(self, A, B):
        return self.BIN.format(self, self, A), self.BIN.format(self, self, B)

    def __mkpath_bin(self):
        path = os.path.join(self.DESTINATION, '{}/{}___{}/BIN'.format(self, self.__job, self.__date))
        try:
            os.makedirs(path)
        except OSError as err:
            ...
        return path

    # DOWNLOAD ZIP FILE --------------------------------------------------------------------------------
    def get_zip(self):
        __zip_name = self.__get_zip_name()
        __zip = self.__get_zip_url()
        __dest = self.__mkpath_zip()

        try:
            response = requests.get(__zip)
        except Exception as err:
            log.error(err)
            self.__last_error = err
            return False

        open('{}/{}'.format(__dest, __zip_name), 'wb').write(response.content)

    def __get_zip_name(self):
        return '{}.zip'.format(self.__job)

    def __get_zip_url(self):
        return self.ZIP.format(self)

    def __mkpath_zip(self):
        path = os.path.join(self.DESTINATION, '{}/{}___{}/ZIP'.format(self, self.__job, self.__date))
        try:
            os.makedirs(path)
        except OSError as err:
            ...
        return path

    # DOWNLOAD DEB PACKAGE -----------------------------------------------------------------------------
    def get_deb(self):
        __deb_name = self.__get_deb_name()
        __deb = self.__get_deb_url(__deb_name)
        __dest = self.__mkpath_deb()

        try:
            response = requests.get(__deb)
        except Exception as err:
            log.error(err)
            self.__last_error = err
            return False

        open('{}/{}'.format(__dest, __deb_name), 'wb').write(response.content)

    def __get_deb_name(self):
        return self.DEB_PACK.format(self, self.__job)

    def __get_deb_url(self, deb_name):
        return self.DEB.format(self, deb_name)

    def __mkpath_deb(self):
        path = os.path.join(self.DESTINATION, '{}/{}___{}/DEB'.format(self, self.__job, self.__date))
        try:
            os.makedirs(path)
        except OSError as err:
            ...
        return path

    @property
    def last_error(self):
        return self.__last_error

    @property
    def job(self):
        return self.__job

    @job.setter
    def job(self, data):
        log.info(self.__job)
        self.__job = data
        log.info(self.__job)

    @property
    def date(self):
        return self.__date







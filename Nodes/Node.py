# -- coding: utf-8 --
from __future__ import unicode_literals
from abc import ABC, abstractmethod
from Arsenal.Chronicler import log


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


class Node:
    def __init__(self):
        self.__fields = {'Version', 'UnVersion' 'LastSuccessful', 'LastUnsuccessful', 'Duration', 'Weather',
                         'CurrentState'}
        self.test = 'try'

    def get(self, whom, **what):
        ...

    def set(self, whom, **what):
        log.info(whom)
        log.info(what)


if __name__ == '__main__':
    node = Node()
    node.set(whom=__name__, version='12', type='Climate')


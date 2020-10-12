# -- coding: utf-8 --
from __future__ import unicode_literals
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from Arsenal.UnZip import Zip
from Arsenal.Chronicler import log
import os


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


class ScanDisk:
    def __init__(self, directory_to_watch):
        self.observer = Observer()
        self.__dtw = directory_to_watch

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.__dtw, recursive=True)
        self.observer.start()

    def scan_disc(self):
        log.info(os.listdir(self.__dtw))
        job = []
        for __job in os.listdir(self.__dtw):
            try:
                job.append(int(__job.split('___')[0]))
            except Exception as err:
                log.error(__job)
                log.error(err)
        job.sort()
        log.info(job[-1])
        return job[-1]


class Handler(FileSystemEventHandler):
    @staticmethod
    def on_any_event(event):
        if event.is_directory and event.event_type == 'created' and 'ZIP' in event.src_path:
            # log.info('Directory {}'.format(event.src_path))
            ...

        elif event.event_type == 'created' and event.event_type == 'created' and '.zip' in event.src_path:
            # Take any action here when a file is first created.
            log.info("Received created event - %s" % event.src_path)
            Zip.zip_reload(event.src_path)



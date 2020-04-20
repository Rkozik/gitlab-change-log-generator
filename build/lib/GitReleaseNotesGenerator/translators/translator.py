import queue
from abc import ABCMeta, abstractmethod


class Translator:
    __metaclass__ = ABCMeta

    def __init__(self, document):
        self.document = document
        self.log = queue.Queue()

    @abstractmethod
    def translate(self):
        """
        Preforms the pipes and filters necessary to translate a cmd output
        :return:
        """
        pass

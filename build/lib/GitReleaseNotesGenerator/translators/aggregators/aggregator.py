from abc import ABCMeta, abstractmethod
from queue import Queue


class Aggregator:
    __metaclass__ = ABCMeta

    def __init__(self, log: Queue):
        self.log = log

    @abstractmethod
    def aggregate(self):
        """
        Preforms the sequences of steps necessary to assemble commits
        :return:
        """
        pass

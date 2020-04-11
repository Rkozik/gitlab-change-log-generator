from abc import ABCMeta, abstractmethod


class IExtractor:
    __metaclass__ = ABCMeta

    @abstractmethod
    def execute(self): raise NotImplementedError

    @abstractmethod
    def save(self): raise NotImplementedError

    @abstractmethod
    def load(self): raise NotImplementedError

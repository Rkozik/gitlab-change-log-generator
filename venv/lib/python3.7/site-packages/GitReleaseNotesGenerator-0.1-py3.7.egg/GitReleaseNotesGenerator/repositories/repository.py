from abc import ABCMeta, abstractmethod


class Repository:
    __metaclass__ = ABCMeta

    def __init__(self):
        self.object_list = {}

    def count(self):
        return len(self.object_list)

    def list(self):
        return self.object_list

    @abstractmethod
    def has(self, object_id: str) -> bool:
        pass

    @abstractmethod
    def get(self, object_id: str):
        pass

    @abstractmethod
    def add(self, object: object):
        pass

    @abstractmethod
    def remove(self, commit_hash):
        pass

    def remove_all(self):
        self.object_list = {}

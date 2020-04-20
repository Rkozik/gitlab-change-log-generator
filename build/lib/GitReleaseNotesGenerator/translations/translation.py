from abc import ABCMeta, abstractmethod


class Translation:
    __metaclass__ = ABCMeta

    def __init__(self, phrase: str):
        self.phrase = phrase

    @abstractmethod
    def verify(self) -> bool:
        """
        Determines whether or not the translation is necessary.
        :return:
        """
        pass

    @abstractmethod
    def translate(self):
        """
        Transforms a foreign phrase into a native phrase.
        :return:
        """
        pass

    def apply(self):
        """
        Preforms the translation if it needs to happen.
        :return:
        """
        return self.translate() if self.verify() else self.phrase

    @abstractmethod
    def __regex(self, phrase: str):
        """
        Regular expressions used in content parsing
        :return:
        """
        pass

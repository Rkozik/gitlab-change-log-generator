from GitChangeLogGenerator.translations.translation import Translation
import re


class UserPattern(Translation):
    def __init__(self, phrase: str, regex: str, name: str):
        super().__init__(phrase=phrase)
        self.regex = regex
        self.name = name

    def verify(self) -> bool:
        return True if self.__regex(self.phrase) is not None else False

    def translate(self):
        id = self.__regex(self.phrase).group(1)
        name = self.__regex(self.phrase).group(2) if 2 in self.__regex(self.phrase).groups() else ""
        return {"id": id, "name": name}

    def __regex(self, phrase):
        regex = re.search(r'((?<=bugfix\/)[0-9]+)(.*)', phrase)
        return regex if regex is not None else None
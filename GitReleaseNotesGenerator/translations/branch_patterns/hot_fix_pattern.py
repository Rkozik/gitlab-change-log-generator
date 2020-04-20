from GitReleaseNotesGenerator.translations.translation import Translation
import re


class HotFixPattern(Translation):

    def verify(self) -> bool:
        return True if self.__regex(self.phrase) is not None else False

    def translate(self):
        id = self.__regex(self.phrase).group(1)
        name = self.__regex(self.phrase).group(2) if 2 in self.__regex(self.phrase).groups() else ""
        return {"id": id, "name": name}

    def __regex(self, branch):
        regex = re.search(r'((?<=hotfix\/)[0-9]+)(.*)', branch)
        return regex if regex is not None else None

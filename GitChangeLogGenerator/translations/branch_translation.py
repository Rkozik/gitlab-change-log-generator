from GitChangeLogGenerator.translations.translation import Translation
from GitChangeLogGenerator.utils.utils import Utils
import re


class BranchTranslation(Translation):

    def verify(self) -> bool:
        is_valid = False
        if self.__regex(self.phrase) is not None or Utils().get_sha1(self.phrase) is not None:
            is_valid = True
        return is_valid

    def translate(self):
        branches = self.__regex(self.phrase) if self.__regex(self.phrase) is not None else ""
        return branches.split(',')

    def __regex(self, phrase):
        regex = re.search(r'\(((HEAD ->)|(tag+([a-zA-Z0-9.: ]+,)+))?(.*)\)', phrase)
        return regex.group(5) if regex is not None else None

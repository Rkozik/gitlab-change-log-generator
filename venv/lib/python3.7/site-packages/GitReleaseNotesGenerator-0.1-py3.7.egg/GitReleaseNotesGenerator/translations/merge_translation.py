from GitReleaseNotesGenerator.translations.translation import Translation
import re


class MergeTranslation(Translation):

    def verify(self) -> bool:
        return True if self.__regex(self.phrase) is not None else False

    def translate(self) -> list:
        merge = self.__regex(self.phrase)
        return merge.split()

    def __regex(self, phrase) -> str:
        regex = re.search(r'((Merge:\W)(?=[0-9a-f]{5,40}))(.*)', phrase)
        return regex.group(3) if regex is not None else None

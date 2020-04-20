from GitReleaseNotesGenerator.translations.translation import Translation
from GitReleaseNotesGenerator.utils.git_utils import GitUtils
import re


class CommitHashTranslation(Translation):

    def verify(self) -> bool:
        return True if self.__regex(self.phrase) is not None else False

    def translate(self) -> str:
        long_hash = self.__regex(self.phrase)
        return GitUtils().get_short_sha(long_hash)

    def __regex(self, phrase):
        regex = re.search(r'(commit\W)([0-9a-f]{5,40})', phrase)
        return regex.group(2) if regex is not None else None

from GitChangeLogGenerator.translations.commit_hash_translation import CommitHashTranslation
from GitChangeLogGenerator.translations.branch_translation import BranchTranslation
from GitChangeLogGenerator.translations.tag_translation import TagTranslation
from GitChangeLogGenerator.translations.merge_translation import MergeTranslation
from GitChangeLogGenerator.translations.translation_types import TranslationTypes
from GitChangeLogGenerator.translators.translator import Translator
from GitChangeLogGenerator.translators.aggregators.git_log_aggregator import GitLogAggregator
from GitChangeLogGenerator.utils.utils import Utils
from GitChangeLogGenerator.utils.git_utils import GitUtils


class GitLogTranslator(Translator):
    def __init__(self, document):
        super().__init__(document=document)
        self.translation_types = TranslationTypes

    def translate(self, needle=None):
        for line in self.document:
            if needle is not None and self.__found_needle(needle, line):
                break

            self.__filter(line, CommitHashTranslation(line).apply(), self.translation_types.TRANSLATE_HASH)
            self.__filter(line, BranchTranslation(line).apply(), self.translation_types.TRANSLATE_BRANCHES)
            self.__filter(line, TagTranslation(line).apply(), self.translation_types.TRANSLATE_TAGS)
            self.__filter(line, MergeTranslation(line).apply(), self.translation_types.TRANSLATE_MERGE)

        return GitLogAggregator(self.log).aggregate()

    def __filter(self, line: str, translation: str, translated: TranslationTypes):
        if line != translation:
            self.log.put({translated: translation})

    def __found_needle(self, needle, line) -> bool:
        if Utils().is_sha1(needle) is True:
            haystack = CommitHashTranslation(line).apply()
            needle = GitUtils().get_short_sha(needle)
        else:
            haystack = TagTranslation(line).apply()

        return True if haystack == needle and needle is not None else False

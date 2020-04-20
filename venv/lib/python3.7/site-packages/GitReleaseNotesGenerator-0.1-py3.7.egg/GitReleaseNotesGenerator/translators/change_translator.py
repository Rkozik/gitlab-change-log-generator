from GitReleaseNotesGenerator.translations.branch_patterns.bug_fix_pattern import BugFixPattern
from GitReleaseNotesGenerator.translations.branch_patterns.feature_pattern import FeaturePattern
from GitReleaseNotesGenerator.translations.branch_patterns.hot_fix_pattern import HotFixPattern
from GitReleaseNotesGenerator.translations.branch_patterns.pattern_types import PatternTypes
from GitReleaseNotesGenerator.translators.aggregators.change_aggregator import ChangeAggregator
from GitReleaseNotesGenerator.translators.translator import Translator


class ChangeTranslator(Translator):
    def __init__(self, document):
        super().__init__(document=document)
        self.pattern_types = PatternTypes

    def translate(self):
        for commit in self.document.list():
            for branch in self.document.get(commit).branches:
                self.__filter(branch, BugFixPattern(branch).apply(), self.pattern_types.PATTERN_BUGFIX, commit)
                self.__filter(branch, FeaturePattern(branch).apply(), self.pattern_types.PATTERN_FEATURE, commit)
                self.__filter(branch, HotFixPattern(branch).apply(), self.pattern_types.PATTERN_HOTFIX, commit)

        return ChangeAggregator(self.log).aggregate()

    def __filter(self, line: str, translation, translated: PatternTypes, commit_hash: str):
        if line != translation:
            self.log.put({"commit_hash": commit_hash, translated: translation})

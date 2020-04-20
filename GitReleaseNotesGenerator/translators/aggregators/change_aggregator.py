from GitReleaseNotesGenerator.translators.aggregators.aggregator import Aggregator
from GitReleaseNotesGenerator.translations.branch_patterns.pattern_types import PatternTypes
from GitReleaseNotesGenerator.repositories.change_repository import ChangeRepository
from GitReleaseNotesGenerator.change import Change
from queue import Queue


class ChangeAggregator(Aggregator):
    def __init__(self, log: Queue):
        super().__init__(log=log)
        self.change_log = ChangeRepository()
        self.pattern_types = PatternTypes

    def aggregate(self):
        while not self.log.empty():
            log_item = self.log.get()

            self.__add_to_changes(self.pattern_types.PATTERN_BUGFIX, log_item)
            self.__add_to_changes(self.pattern_types.PATTERN_FEATURE, log_item)
            self.__add_to_changes(self.pattern_types.PATTERN_HOTFIX, log_item)

        return self.change_log

    def __add_to_changes(self, pattern_type: PatternTypes, log_item: dict):
        if pattern_type in log_item:
            new_change = Change(commit_hash=log_item["commit_hash"],
                                id=log_item[pattern_type]["id"],
                                name=log_item[pattern_type]["name"],
                                type=pattern_type)
            self.change_log.add(new_change)
            self.change_log.register_type(commit_hash=log_item["commit_hash"], type=pattern_type)

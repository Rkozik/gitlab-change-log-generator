from GitChangeLogGenerator.commit.commit import Commit
from GitChangeLogGenerator.commit.tag_commit import TagCommit
from GitChangeLogGenerator.commit.merge_commit import MergeCommit
from GitChangeLogGenerator.translators.aggregators.aggregator import Aggregator
from GitChangeLogGenerator.translations.translation_types import TranslationTypes
from GitChangeLogGenerator.repositories.log_repository import LogRepository
from queue import Queue


class GitLogAggregator(Aggregator):
    def __init__(self, log: Queue):
        super().__init__(log=log)
        self.log_repository = LogRepository()
        self.translation_types = TranslationTypes
        self.commit = {}

    def aggregate(self):
        while not self.log.empty():
            log_item = self.log.get()

            if self.commit != {} and self.translation_types.TRANSLATE_HASH in log_item:
                new_commit = self.__commit_factory()
                self.log_repository.add(new_commit)
                self.commit = {}

            self.__add_to_commit(self.translation_types.TRANSLATE_HASH, log_item)
            self.__add_to_commit(self.translation_types.TRANSLATE_BRANCHES, log_item)
            self.__add_to_commit(self.translation_types.TRANSLATE_TAGS, log_item)
            self.__add_to_commit(self.translation_types.TRANSLATE_MERGE, log_item)

        return self.log_repository

    def __add_to_commit(self, translation_type: TranslationTypes, log_item: dict):
        if translation_type in log_item:
            self.commit[translation_type] = log_item[translation_type]

    def __commit_factory(self):
        if self.translation_types.TRANSLATE_TAGS in self.commit:
            new_commit = TagCommit(commit_hash=self.commit[self.translation_types.TRANSLATE_HASH],
                                   branches=self.commit[self.translation_types.TRANSLATE_BRANCHES],
                                   tags=self.commit[self.translation_types.TRANSLATE_TAGS])

        elif self.translation_types.TRANSLATE_MERGE in self.commit:
            new_commit = MergeCommit(commit_hash=self.commit[self.translation_types.TRANSLATE_HASH],
                                     branches=self.commit[self.translation_types.TRANSLATE_BRANCHES],
                                     merge=self.commit[self.translation_types.TRANSLATE_MERGE])

        else:
            new_commit = Commit(commit_hash=self.commit[self.translation_types.TRANSLATE_HASH],
                                branches=self.commit[self.translation_types.TRANSLATE_BRANCHES])

        return new_commit

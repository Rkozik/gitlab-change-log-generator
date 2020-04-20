from GitReleaseNotesGenerator.translations.branch_patterns.pattern_types import PatternTypes
from GitReleaseNotesGenerator.repositories.repository import Repository
from GitReleaseNotesGenerator.change import Change


class ChangeRepository(Repository):
    def __init__(self):
        super().__init__()
        self.type_list = {}

    def has(self, commit_hash: str) -> bool:
        return True if commit_hash in self.object_list else False

    def get(self, commit_hash: str):
        if self.object_list[commit_hash]:
            return self.object_list[commit_hash]
        else:
            raise Exception('Commit does not exist.')

    def add(self, change: Change):
        self.object_list[change.commit_hash] = change

    def remove(self, commit_hash: str):
        if self.object_list[commit_hash]:
            del self.object_list[commit_hash]
        else:
            raise Exception('Commit does not exist.')

    def register_type(self, commit_hash: str, type: PatternTypes):
        if type.value not in self.type_list:
            self.type_list[type.value] = []

        self.type_list[type.value].append(commit_hash)

    def get_type(self, type: PatternTypes):
        change_list = []
        if type.value in self.type_list:
            for commit_hash in self.type_list[type.value]:
                change_list.append(self.get(commit_hash))

        return change_list

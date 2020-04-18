from GitChangeLogGenerator.repositories.repository import Repository
from GitChangeLogGenerator.change import Change


class ChangeRepository(Repository):
    def has(self, commit_hash: str) -> bool:
        return True if commit_hash in self.object_list else False

    def get(self, commit_hash: str):
        if self.object_list[commit_hash]:
            return self.object_list[commit_hash]
        else:
            raise Exception('Commit does not exist.')

    def add(self, change: Change):
        self.object_list[change.commit_hash] = change

    def remove(self, commit_hash):
        if self.object_list[commit_hash]:
            del self.object_list[commit_hash]
        else:
            raise Exception('Commit does not exist.')

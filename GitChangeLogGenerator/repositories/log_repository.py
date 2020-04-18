from GitChangeLogGenerator.repositories.repository import Repository
from GitChangeLogGenerator.commit import commit


class LogRepository(Repository):
    def has(self, commit_hash: str) -> bool:
        return True if commit_hash in self.object_list else False

    def get(self, commit_hash: str):
        if self.object_list[commit_hash]:
            return self.object_list[commit_hash]
        else:
            raise Exception('Commit does not exist.')

    def add(self, commit: commit):
        self.object_list[commit.commit_hash] = commit

    def remove(self, commit_hash):
        if self.object_list[commit_hash]:
            del self.object_list[commit_hash]
        else:
            raise Exception('Commit does not exist.')

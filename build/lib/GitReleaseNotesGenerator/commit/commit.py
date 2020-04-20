from GitReleaseNotesGenerator.utils.git_utils import GitUtils
from abc import ABCMeta


class Commit:
    __metaclass__ = ABCMeta

    def __init__(self, commit_hash: str, branches: list):
        self.commit_hash = commit_hash
        self.branches = branches
        self.git_utils = GitUtils()

    def get_author_name(self) -> str:
        return self.git_utils.get_commit_author_name(self.commit_hash)

    def get_author_email(self) -> str:
        return self.git_utils.get_commit_author_email(self.commit_hash)

    def get_subject(self) -> str:
        return self.git_utils.get_commit_subject(self.commit_hash)

    def get_body(self) -> str:
        return self.git_utils.get_commit_body(self.commit_hash)

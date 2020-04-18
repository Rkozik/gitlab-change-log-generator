from GitChangeLogGenerator.commit.commit import Commit


class TagCommit(Commit):
    def __init__(self, commit_hash: str, branches, tags):
        super().__init__(commit_hash=commit_hash, branches=branches)
        self.tags = tags

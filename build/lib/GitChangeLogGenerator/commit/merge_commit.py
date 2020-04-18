from GitChangeLogGenerator.commit.commit import Commit
from GitChangeLogGenerator.utils.git_utils import GitUtils


class MergeCommit(Commit):
    def __init__(self, commit_hash: str, branches, merge: list):
        super().__init__(commit_hash=commit_hash, branches=branches)
        self.merge = merge

    def get_merged_with(self):
        return GitUtils().get_branch_names(self.merge[1])

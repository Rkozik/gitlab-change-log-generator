from GitReleaseNotesGenerator.utils.utils import Utils
from GitReleaseNotesGenerator.translations.branch_translation import BranchTranslation


class GitUtils:
    def __init__(self):
        self.utils = Utils()

    def get_short_sha(self, long_sha: str):
        short_sha_cmd = "git rev-parse --short " + long_sha
        output = self.utils.get_cmd_output(cmd=short_sha_cmd)[0]
        return self.utils.get_sha1(output)

    def get_tag_short_sha(self, tag: str):
        short_sha_cmd = "git rev-parse --short " + tag
        output = self.utils.get_cmd_output(cmd=short_sha_cmd)[0]
        return self.utils.get_sha1(output)

    def get_commit_author_name(self, commit_hash: str) -> str:
        get_author_cmd = "git log -n 1 --format='%aN' " + commit_hash
        return self.utils.get_cmd_output(cmd=get_author_cmd)[0]

    def get_commit_author_email(self, commit_hash: str) -> str:
        get_author_email_cmd = "git log -n 1 --format='%aE' " + commit_hash
        return self.utils.get_cmd_output(cmd=get_author_email_cmd)[0]

    def get_commit_subject(self, commit_hash: str) -> str:
        get_subject_cmd = "git log -n 1 --format='%s' " + commit_hash
        return self.utils.get_cmd_output(cmd=get_subject_cmd)[0]

    def get_commit_body(self, commit_hash: str) -> str:
        get_body_cmd = "git log -n 1 --format='%b' " + commit_hash
        return self.utils.get_cmd_output(cmd=get_body_cmd)

    def get_commit_timestamp(self, commit_hash: str) -> int:
        get_timestamp_cmd = "git log -n 1 --format='%at' " + commit_hash
        return int(self.utils.get_cmd_output(cmd=get_timestamp_cmd)[0])

    def is_tag(self, commit_hash: str) -> bool:
        is_tag_cmd = "git tag --points-at " + commit_hash
        return True if self.utils.get_cmd_output(cmd=is_tag_cmd)[0] != "" else False

    def get_branch_names(self, commit_hash: str):
        get_branch_names_cmd = "git log -in " + commit_hash
        line_1 = self.utils.get_cmd_output(get_branch_names_cmd)[0]
        return BranchTranslation(line_1).apply()

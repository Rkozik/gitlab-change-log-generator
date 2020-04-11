from commits.Commit import Commit
import subprocess
import re


class MergeCommit(Commit):

    def __init__(self, hash: str, author_name: str, author_email: str, author_date: str, commit_name: str,
                 commit_email: str, commit_date: str, subject: str, body: str, branch="", merged_into=""):
        super().__init__(hash=hash, author_name=author_name, author_email=author_email, author_date=author_date,
                         commit_name=commit_name, commit_email=commit_email, commit_date=commit_date,
                         subject=subject, body=body, branch=branch)
        self.merged_into = merged_into if merged_into != "" else ""

    def set_merged_with(self, merged_into: str, project_directory: str):
        cmd = "cd " + project_directory + "; git name-rev --name-only " + merged_into
        output = subprocess.check_output(cmd, shell=True).decode("ISO-8859-1")
        is_branch_ref = re.search(r'((?<=remotes\/)|(?<=tags\/))([a-zA-Z0-9_\/]+)(?=)', output)

        if is_branch_ref is None:
            sha1 = re.search(r'([0-9a-f]{5,40})(?=~)', output)
            if sha1 is not None:
                sha1 = sha1.group(1)
                cmd_shorten_sha = "cd " + project_directory + "; git rev-parse --short " + sha1
                shortened_sha = subprocess.check_output(cmd_shorten_sha, shell=True).decode("ISO-8859-1").splitlines()[0]
                cmd_branch_name = "cd " + project_directory + "; git branch --contains " + shortened_sha
                branch_name = subprocess.check_output(cmd_branch_name, shell=True).decode("ISO-8859-1").splitlines()[1][2:]
                self.merged_into = branch_name
            else:
                self.merged_into = output
        else:
            self.merged_into = is_branch_ref.group(2)

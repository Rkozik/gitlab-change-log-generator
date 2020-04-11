from abc import ABCMeta, abstractmethod
import subprocess
import re


class Commit:
    __metaclass__ = ABCMeta

    def __init__(self, hash: str, author_name: str, author_email: str, author_date: str, commit_name: str,
                 commit_email: str, commit_date: str, subject: str, body: str, branch=""):
        self.hash = hash
        self.author_name = author_name
        self.author_email = author_email
        self.author_date = author_date
        self.commit_name = commit_name
        self.commit_email = commit_email
        self.commit_date = commit_date
        self.subject = subject
        self.body = body
        self.branch = branch if branch != "" else ""

    def set_branch_name(self, project_directory: str):
        cmd = "cd " + project_directory + "; git name-rev --name-only " + self.hash
        output = subprocess.check_output(cmd, shell=True).decode("ISO-8859-1")
        is_branch_ref = re.search(r'((?<=remotes\/)|(?<=tags\/))([a-zA-Z0-9_\/]+)(?=)', output)

        if is_branch_ref is None:
            sha1 = re.search(r'([0-9a-f]{5,40})(?=~)', output)
            if sha1 is not None:
                sha1 = sha1.group(1)
                cmd_shorten_sha = "cd " + project_directory + "; git rev-parse --short " + sha1
                shortened_sha = subprocess.check_output(cmd_shorten_sha, shell=True).decode("ISO-8859-1").splitlines()[
                    0]
                cmd_branch_name = "cd " + project_directory + "; git branch --contains " + shortened_sha
                branch_name = subprocess.check_output(cmd_branch_name, shell=True).decode("ISO-8859-1").splitlines()[1][
                              2:]
                self.branch = branch_name
            else:
                self.branch = output
        else:
            self.branch = is_branch_ref.group(2)

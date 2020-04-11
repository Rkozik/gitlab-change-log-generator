from extractors.IExtractor import IExtractor
from commits.Commit import Commit
from utils.Utils import Utils
import subprocess
import json
import os.path


class GitCommitExtractor(IExtractor):
    def __init__(self, project_directory):
        self.project_directory = project_directory
        self.commits = {}

    def execute(self):
        merges_cmd = "cd " + self.project_directory + "; " \
            "git --no-pager log --decorate --pretty=\"" \
            "format:" \
            "Hash:%h%n" \
            "Author Name:%aN%n" \
            "Author Email:%aE%n" \
            "Author Date:%at%n" \
            "Commit Name:%cN%n" \
            "Commit Email:%cE%n" \
            "Commit Date:%ct%n" \
            "Subject:%s%n" \
            "Body:%B%n" \
            "===END===\""

        output = subprocess.check_output(merges_cmd, shell=True).decode("ISO-8859-1").splitlines()

        commit = {}
        i = 0
        for line in output:
            commit = Utils().parse_commit_object(line=line, commit=commit)

            if line == "===END===":
                i += 1
                new_commit = Commit(
                    hash=commit["hash"], author_name=commit["author_name"], author_email=commit["author_email"],
                    author_date=commit["author_date"], commit_name=commit["commit_name"],
                    commit_email=commit["commit_email"], commit_date=commit["commit_date"], subject=commit["subject"],
                    body=commit["body"])
                new_commit.set_branch_name(self.project_directory)

                self.commits[new_commit.hash] = new_commit
                commit = {}

                if i == 4:
                    break



from extractors.IExtractor import IExtractor
from commits.MergeCommit import MergeCommit
from utils.Utils import Utils
import subprocess
import json
import os.path


class GitMergeLogExtractor(IExtractor):
    def __init__(self, project_directory):
        self.project_directory = project_directory
        self.merge_commits = self.load()

    def execute(self):
        merges_cmd = "cd " + self.project_directory + "; " \
            "git --no-pager log --merges --decorate --pretty=\"" \
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
            "\""

        output = subprocess.check_output(merges_cmd, shell=True).decode("ISO-8859-1").splitlines()

        commit = {}
        for line in output:
            commit = Utils().parse_commit_object(line=line, commit=commit)

            if line == "" and commit != {} and commit["hash"] not in self.merge_commits:
                new_commit = MergeCommit(
                    hash=commit["hash"], author_name=commit["author_name"], author_email=commit["author_email"],
                    author_date=commit["author_date"], commit_name=commit["commit_name"],
                    commit_email=commit["commit_email"], commit_date=commit["commit_date"], subject=commit["subject"],
                    body=commit["body"])
                new_commit.set_branch_name(self.project_directory)

                cmd_gitshow = "git --no-pager show " + new_commit.hash
                output = subprocess.check_output("cd " + self.project_directory + "; " + cmd_gitshow, shell=True)
                merge_line = output.decode("ISO-8859-1").splitlines()[1]
                merged_into = merge_line.split('Merge: ')[1].split(' ')[0]
                new_commit.set_merged_with(merged_into, self.project_directory)

                self.merge_commits[new_commit.hash] = new_commit
                commit = {}

        self.save()

    def load(self):
        json_file = open("cache/merge_commits.json", mode="r") if os.path.isfile("cache/merge_commits.json") else None
        merge_commits = {}
        if json_file is not None:
            json_merge_commits = json.loads(json_file.readline())
            for merge_commit in json_merge_commits:
                new_commit = MergeCommit(
                    hash=json_merge_commits[merge_commit]["hash"],
                    author_name=json_merge_commits[merge_commit]["author_name"],
                    author_email=json_merge_commits[merge_commit]["author_email"],
                    author_date=json_merge_commits[merge_commit]["author_date"],
                    commit_name=json_merge_commits[merge_commit]["commit_name"],
                    commit_email=json_merge_commits[merge_commit]["commit_email"],
                    commit_date=json_merge_commits[merge_commit]["commit_date"],
                    subject=json_merge_commits[merge_commit]["subject"],
                    body=json_merge_commits[merge_commit]["body"],
                    branch=json_merge_commits[merge_commit]["branch"],
                    merged_into=json_merge_commits[merge_commit]["merged_into"]
                )

                merge_commits[new_commit.hash] = new_commit
            json_file.close()
        return merge_commits

    def save(self):
        merge_commits = {}
        for merge_commit in self.merge_commits:
            merge_commits[merge_commit] = self.merge_commits[merge_commit].__dict__

        json_merge_commits = json.dumps(merge_commits)
        json_file = open("cache/merge_commits.json", mode="w+")
        json_file.write(json_merge_commits)
        json_file.close()

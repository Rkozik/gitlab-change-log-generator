from extractors.IExtractor import IExtractor
from commits.TagCommit import TagCommit
from utils.Utils import Utils
import subprocess
import json
import os.path


class GitTagsExtractor(IExtractor):
    def __init__(self, project_directory):
        self.project_directory = project_directory
        self.tag_commits = self.load()

    def execute(self):
        tags_cmd = "cd " + self.project_directory + "; " \
            "git --no-pager log --tags --decorate --pretty=\"" \
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
        output = subprocess.check_output(tags_cmd, shell=True).decode("ISO-8859-1").splitlines()

        commit = {}
        for line in output:
            commit = Utils().parse_commit_object(line=line, commit=commit)

            if line == "" and commit != {} and commit["hash"] not in self.tag_commits:
                new_commit = TagCommit(
                    hash=commit["hash"], author_name=commit["author_name"], author_email=commit["author_email"],
                    author_date=commit["author_date"], commit_name=commit["commit_name"],
                    commit_email=commit["commit_email"], commit_date=commit["commit_date"], subject=commit["subject"],
                    body=commit["body"])
                new_commit.set_branch_name(self.project_directory)

                self.tag_commits[new_commit.hash] = new_commit
                commit = {}

        self.save()

    def load(self):
        json_file = open("cache/tag_commits.json", mode="r") if os.path.isfile("cache/tag_commits.json") else None
        tag_commits = {}
        if json_file is not None:
            json_tag_commits = json.loads(json_file.readline())
            for merge_commit in json_tag_commits:
                new_commit = TagCommit(
                    hash=json_tag_commits[merge_commit]["hash"],
                    author_name=json_tag_commits[merge_commit]["author_name"],
                    author_email=json_tag_commits[merge_commit]["author_email"],
                    author_date=json_tag_commits[merge_commit]["author_date"],
                    commit_name=json_tag_commits[merge_commit]["commit_name"],
                    commit_email=json_tag_commits[merge_commit]["commit_email"],
                    commit_date=json_tag_commits[merge_commit]["commit_date"],
                    subject=json_tag_commits[merge_commit]["subject"],
                    body=json_tag_commits[merge_commit]["body"],
                    branch=json_tag_commits[merge_commit]["branch"]
                )

                tag_commits[new_commit.hash] = new_commit
            json_file.close()
        return tag_commits

    def save(self):
        tag_commits = {}
        for tag_commit in self.tag_commits:
            tag_commits[tag_commit] = self.tag_commits[tag_commit].__dict__

        json_tag_commits = json.dumps(tag_commits)
        json_file = open("cache/tag_commits.json", mode="w+")
        json_file.write(json_tag_commits)
        json_file.close()


import click
import subprocess
import re


class Utils:

    def get_cmd_output(self, cmd: str):
        return subprocess.check_output(cmd, shell=True).decode("ISO-8859-1").splitlines()

    def is_sha1(self, string: str) -> bool:
        regex = re.search(r'[0-9a-f]{5,40}', string)
        return True if regex is not None else False

    def is_sha1_list(self, list) -> bool:
        is_sha_list = True
        for item in list:
            if self.is_sha1(item) is False:
                is_sha_list = False

        return is_sha_list

    def get_sha1(self, string: str):
        regex = re.search(r'[0-9a-f]{5,40}', string)
        return regex.group() if regex is not None else None

    def click_is_commit(self, value):
        git_commit_cmd = "git cat-file -t " + value
        git_commit = Utils().get_cmd_output(git_commit_cmd)[0]
        if git_commit != "commit":
            raise click.UsageError("The tag or commit you entered is invalid")
        return value

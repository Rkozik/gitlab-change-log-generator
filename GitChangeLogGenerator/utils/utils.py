import subprocess
import re


class Utils:

    def get_cmd_output(self, cmd: str):
        return subprocess.check_output("cd /Users/robertkozik/PycharmProjects/git-change-log-generator; "
                                       + cmd, shell=True).decode("ISO-8859-1").splitlines()

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

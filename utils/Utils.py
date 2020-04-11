class Utils:
    def parse_commit_object(self, line: str, commit: dict):

        if line[0:5] == "Hash:":
            commit["hash"] = line[5:]

        if line[0:12] == "Author Name:":
            commit["author_name"] = line[12:]

        if line[0:13] == "Author Email:":
            commit["author_email"] = line[13:]

        if line[0:12] == "Author Date:":
            commit["author_date"] = line[12:]

        if line[0:12] == "Commit Name:":
            commit["commit_name"] = line[12:]

        if line[0:13] == "Commit Email:":
            commit["commit_email"] = line[13:]

        if line[0:12] == "Commit Date:":
            commit["commit_date"] = line[12:]

        if line[0:8] == "Subject:":
            commit["subject"] = line[8:]

        if line[0:5] == "Body:":
            commit["body"] = line[5:]

        return commit

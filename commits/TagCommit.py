from commits.Commit import Commit


class TagCommit(Commit):

    def __init__(self, hash: str, author_name: str, author_email: str, author_date: str, commit_name: str,
                 commit_email: str, commit_date: str, subject: str, body: str, branch=""):
        super().__init__(hash=hash, author_name=author_name, author_email=author_email, author_date=author_date,
                         commit_name=commit_name, commit_email=commit_email, commit_date=commit_date,
                         subject=subject, body=body, branch=branch)

    def get_tag_name(self):
        return self.branch

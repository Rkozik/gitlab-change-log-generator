from GitReleaseNotesGenerator.translations.branch_patterns.pattern_types import PatternTypes


class Change:
    def __init__(self, id: int, name: str, type: PatternTypes, commit_hash: str):
        self.id = id
        self.name = name
        self.type = type
        self.commit_hash = commit_hash

    def get_name(self):
        return self.name.replace('-', ' ').lstrip()

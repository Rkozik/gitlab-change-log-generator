class Change:
    def __init__(self, id: int, name: str, commit_hash: str):
        self.id = id
        self.name = name
        self.commit_hash = commit_hash

    def get_name(self):
        return self.name.replace('-', ' ')

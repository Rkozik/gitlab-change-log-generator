from extractors.GitMergeExtractor import GitMergeExtractor
from extractors.GitTagsExtractor import GitTagsExtractor
from extractors.GitCommitExtractor import GitCommitExtractor


def main():
    # merge_extractor = GitMergeExtractor("/Users/robertkozik/sites/php2/")
    # merge_extractor.execute()
    # merge_commits = merge_extractor.merge_commits
    #
    # tag_extractor = GitTagsExtractor("/Users/robertkozik/sites/php2/")
    # tag_extractor.execute()
    # tag_commits = tag_extractor.tag_commits

    commit_extractor = GitCommitExtractor("/Users/robertkozik/PycharmProjects/git-change-log-generator")
    commit_extractor.execute()


def find_valid_merge_commits(merge_commits: dict, tag_commits: dict):
    most_recent_tag_hash = next(iter(tag_commits))
    branches_in_release = {}
    for merge_commit in merge_commits:
        if merge_commits[merge_commit].commit_date > tag_commits[most_recent_tag_hash].commit_date:
            branches_in_release[merge_commits[merge_commit].branch] = ""

    print(branches_in_release.__len__())


if __name__ == "__main__":
    main()

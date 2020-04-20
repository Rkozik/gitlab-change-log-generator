from GitReleaseNotesGenerator.results.result import Result
from GitReleaseNotesGenerator.utils.utils import Utils
import click
import subprocess


def validate_tag_or_commit_hash(ctx, value):
    if value != "Default is next tag in commit history following the release <tag> or <commit_hash>":
        try:
            git_commit_cmd = "git cat-file -t " + value
            git_commit = Utils().get_cmd_output(git_commit_cmd)[0]
        except subprocess.CalledProcessError:
            raise click.BadParameter("The <tag> or <commit hash> you entered doesn't exist.")
        return value


@click.command()
@click.option(
    '--current-release',
    required=True,
    prompt="Enter the current release <tag> or <commit_hash>",
    callback=validate_tag_or_commit_hash
)
@click.option(
    '--previous-release',
    prompt="What was the previous release? <tag> or <commit_hash>",
    default='Default is next tag in commit history following the release <tag> or <commit_hash>',
    callback=validate_tag_or_commit_hash
)
@click.option(
    '--project-url',
    required=True,
    prompt="Enter your GitLab project's issue URL",
)
def main(current_release, previous_release, project_url):
    if previous_release == 'Default is next tag in commit history following the release <tag> or <commit_hash>':
        previous_release = None

    result = Result(current_release=current_release, previous_release=previous_release, project_url=project_url)
    result.show()


if __name__ == "__main__":
    main()

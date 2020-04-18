from GitChangeLogGenerator.translators.git_log_translator import GitLogTranslator
from GitChangeLogGenerator.translators.change_translator import ChangeTranslator
from GitChangeLogGenerator.utils.utils import Utils
import click


@click.command()
@click.option('--project-name', required=True, prompt="Enter your project's name")
def main(project_name):
    git_log_cmd = "git --no-pager log --decorate"
    git_log = Utils().get_cmd_output(git_log_cmd)

    log_translator = GitLogTranslator(git_log)
    log_translation = log_translator.translate(needle=None)

    change_translator = ChangeTranslator(log_translation)
    change_translation = change_translator.translate()

    # TODO: Setup test cases for branch patterns


@click.command()
@click.option('--branch-pattern', '-b', multiple=True)
def test(branch_pattern):
    print(branch_pattern)


if __name__ == "__main__":
    test()

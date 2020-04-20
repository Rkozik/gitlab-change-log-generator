from GitReleaseNotesGenerator.translations.branch_patterns.pattern_types import PatternTypes
from GitReleaseNotesGenerator.translators.git_log_translator import GitLogTranslator
from GitReleaseNotesGenerator.translators.change_translator import ChangeTranslator
from GitReleaseNotesGenerator.repositories.log_repository import LogRepository
from GitReleaseNotesGenerator.repositories.change_repository import ChangeRepository
from GitReleaseNotesGenerator.utils.utils import Utils
from GitReleaseNotesGenerator.utils.git_utils import GitUtils
from abc import ABCMeta, abstractmethod
from datetime import datetime
import pystache
from pathlib import Path
import os


class Result:
    __metaclass__ = ABCMeta

    def __init__(self, current_release: str, previous_release: str, project_url: str):
        self.current_release = current_release
        self.previous_release = previous_release
        self.project_url = project_url
        self.template = 'default.txt'

    def show(self):
        git_log = self.get_git_log()
        change_log = self.get_change_log(git_log)

        change_properties = self.get_changes_objects(change_log)
        default_properties = {
            'release_version': self.current_release,
            'release_date': self.get_release_date(self.current_release),
            'project_url': self.project_url
        }
        template_properties = dict(list(change_properties.items()) + list(default_properties.items()))

        templates_path = str(Path(os.path.dirname(__file__)).resolve().parent) + '/templates/'
        template = open(templates_path + self.template, mode='r').read()

        print("====START OUTPUT====")
        print(pystache.render(template, template_properties))
        print("==== END OUTPUT====")

    @abstractmethod
    def get_changes_objects(self, change_repository: ChangeRepository):
        features = self.get_type_changes(change_repository, PatternTypes.PATTERN_FEATURE)
        bug_fixes = self.get_type_changes(change_repository, PatternTypes.PATTERN_BUGFIX)
        hot_fixes = self.get_type_changes(change_repository, PatternTypes.PATTERN_HOTFIX)

        return {'features': features, 'bug_fixes': bug_fixes, 'hot_fixes': hot_fixes}

    @abstractmethod
    def get_type_changes(self, change_repository: ChangeRepository, pattern_type: PatternTypes):
        changes = []
        for change in change_repository.get_type(pattern_type):
            changes.append({
                'name': change.get_name().title(),
                'id': change.id
            })
        return changes

    def get_git_log(self) -> LogRepository:
        git_log_cmd = "git --no-pager log --decorate"
        git_log = Utils().get_cmd_output(git_log_cmd)

        log_translator = GitLogTranslator(git_log)
        return log_translator.translate(needle=self.previous_release)

    def get_change_log(self, git_log: LogRepository) -> ChangeRepository:
        change_translator = ChangeTranslator(git_log)
        return change_translator.translate()

    def get_release_date(self, release):
        release_commit = GitUtils().get_tag_short_sha(release)
        release_date = GitUtils().get_commit_timestamp(release_commit)
        return datetime.utcfromtimestamp(release_date).strftime('%Y-%m-%d')

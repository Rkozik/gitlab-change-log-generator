from enum import Enum


class TranslationTypes(Enum):
    TRANSLATE_HASH = "Hash"
    TRANSLATE_BRANCHES = "Branches"
    TRANSLATE_MERGE = "Merge"
    TRANSLATE_TAGS = "Tags"

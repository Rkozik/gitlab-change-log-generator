from GitChangeLogGenerator.translations.translation import Translation
import re


class TagTranslation(Translation):

    def verify(self) -> bool:
        return True if self.__regex(self.phrase) is not None else False

    def translate(self):
        return self.__regex(self.phrase) if self.__regex(self.phrase) != [] else self.phrase

    def __regex(self, phrase):
        regex = re.findall(r'(?<=tag: )+([a-zA-Z0-9.]+)+', phrase)
        return regex if regex is not None else None

import string

from .validator import IValidator

punctuation = r"""!"#$%&'()*+./:;<=>?@[\]^_`{|}~"""


class EntryValidator(IValidator):
    def __init__(self, params: dict):
        self.params: dict[str, str] = params
        self.errors: list[tuple[str]] = []

    def isValid(self):
        valid = True
        for key, value in self.params.items():
            isDigits = False
            isPunctuations = False
            if isinstance(value, str):
                for ch in value:
                    if ch in string.digits and not isDigits:
                        self.errors.append(
                            'Field {} contains digits'.format(key[1:].upper()))
                        valid = False
                        isDigits = True
                    if ch in punctuation and not isPunctuations:
                        self.errors.append(
                            'Field {} containts punctuation symbols'.format(
                                key[1:].upper())
                        )
                        valid = False
                        isPunctuations = True
        return valid, self.errors

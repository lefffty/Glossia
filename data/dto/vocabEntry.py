from dataclasses import dataclass


@dataclass
class VocabEntry:
    entry_id: int
    word: str
    translation: str

    @classmethod
    def from_dict(cls, params):
        return cls(**params)

    def to_string(self) -> str:
        _format = '{} - {}'
        return _format.format(self.word, self.translation)

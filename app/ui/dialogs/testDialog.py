from PySide6.QtWidgets import (
    QDialog,
)

from .ui.testDialog_ui import Ui_Dialog


class TestDialog(QDialog, Ui_Dialog):
    def __init__(
        self,
        words: list[str],
        translations: list[str],
        testMode: str,
        parent=None
    ):
        super().__init__(parent)

        self.setupUi(self)

        self._translationInputs: list[str] = []
        self._translations = translations.copy()
        self._words = words.copy()
        self._cursor = 0
        self._testMode = testMode

        self.setupComponents()

    def setupComponents(self):
        self.toNextPairBtn.clicked.connect(self.onToNextPairBtnClicked)

        word = self._words[self._cursor]
        self.wordLineEdit.setText(word)

        self.formatLabel.setEnabled(True)
        self.formatLabel.setText(self._testMode)

    def onToNextPairBtnClicked(self):
        translationInput = self.translationLineEdit.text()
        self.translationLineEdit.clear()
        self._translationInputs.append(translationInput)
        if self._cursor < len(self._words) - 1:
            self._cursor += 1
            word = self._words[self._cursor]
            self.wordLineEdit.setText(word)
        elif self._cursor == len(self._words) - 1:
            self.toNextPairBtn.setEnabled(False)
            self.toFinishBtn.setEnabled(True)

    def onFinishBtnClicked(self):
        pass

    def params(self):
        return {
            'translationInputs': self._translationInputs,
            'translations': self._translations,
            'words': self._words,
        }

from PySide6.QtWidgets import QDialog

from .ui.pairDialog_ui import Ui_Dialog


class PairDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None, record_data=None):
        super().__init__(parent)

        self.record_data = record_data or {}

        self.setupUi(self)
        self.setupComponents()

    def setupComponents(self):
        self.wordLineEdit.setText(self.record_data.get('word', ''))
        self.translationLineEdit.setText(
            self.record_data.get('translation', ''))

        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

    def params(self) -> dict:
        return {
            ':wordId': self.wordLineEdit.text(),
            ':translationId': self.translationLineEdit.text(),
            ':vocabId': self.record_data[':vocabId'],
        }

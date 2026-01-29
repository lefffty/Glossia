from PySide6.QtWidgets import QDialog

from .ui.vocabDialog_ui import Ui_Dialog


class VocabDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)

    def params(self):
        return {
            ':vocabName': self.vocabularyNameLineEdit.text(),
        }

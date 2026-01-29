import sys


from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QListWidgetItem,
    QDialog,
    QFileDialog
)
from PySide6.QtCore import (
    QCoreApplication,
    Qt
)

from ui.mainwindow.mainwindow_ui import Ui_MainWindow
from ui.dialogs.pairDialog import PairDialog
from ui.dialogs.vocabDialog import VocabDialog

from domain.managers.db import DatabaseManager
from domain.managers.entries import VocabularyEntriesManager
from domain.managers.vocabulary import VocabularyManager

from utils.validators.entry import EntryValidator

from data.dto.vocabEntry import VocabEntry


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.role = Qt.ItemDataRole.UserRole

        config_path = self.setupConfig()

        self.setupManagers(config_path)
        self.setupWidgets()
        self._getVocabsList()
        self.show()

    def setupConfig(self):
        config_path = 'config.yaml'
        return config_path

    def setupWidgets(self):
        self.exitBtn.clicked.connect(QCoreApplication.instance().exit)

        self.createVocabBtn.clicked.connect(self.onCreateVocabBtnClicked)
        self.deleteVocabBtn.clicked.connect(self.onDeleteVocabBtnClicked)

        self.vocabsListWidget.itemDoubleClicked.connect(
            self.onVocabDoubleClicked)

        self.addRowBtn.clicked.connect(self.onAddRowBtnClicked)
        self.deleteRowBtn.clicked.connect(self.onDeleteRowBtnClicked)

        self.entriesListWidget.show()

    def setupManagers(self, config_path):
        self.dbManager = DatabaseManager(config_path)
        self.vocabManager = VocabularyManager(self.dbManager)
        self.vocabEntriesManager = VocabularyEntriesManager(self.dbManager)

    def onDeleteVocabBtnClicked(self):
        vocabName = self._getCurrentVocabName()

        reply = QMessageBox.question(
            self,
            'Dictionary removal',
            'Are you sure you want to delete "{}" vocabulary?'.format(
                vocabName),
        )

        if reply == QMessageBox.StandardButton.Yes:
            params = {
                ':vocabName': vocabName,
            }

            self.vocabManager.delete(params)
            self._getVocabsList()
            self.vocabNameLabel.setText('')
            self.vocabWidget.setEnabled(False)

    def onDeleteRowBtnClicked(self):
        if not self.entriesListWidget.count():
            return QMessageBox.warning(
                self,
                'Vocabulary error',
                'Vocabulary is empty!',
            )
        entry = self.entriesListWidget.currentItem().data(self.role)
        parts = entry.split(' - ')
        vocabName = self._getCurrentVocabName()
        word, translation = parts[0], parts[1]
        params = {
            'word': word,
            'translation': translation,
            'vocabName': vocabName,
        }
        self.vocabEntriesManager.delete(params)
        self.onVocabDoubleClicked()

    def onAddRowBtnClicked(self):
        record_data = {
            ':vocabId': self._getCurrentVocabName(),
        }

        dialog = PairDialog(self, record_data)

        if dialog.exec() == QDialog.DialogCode.Accepted:
            params = dialog.params()

            validator = EntryValidator(params)

            valid, errors = validator.isValid()

            if not valid:
                QMessageBox.information(
                    self,
                    'Error',
                    '\n'.join(errors),
                )
            else:
                self.vocabEntriesManager.create(params)
                self.onVocabDoubleClicked()

    def onVocabDoubleClicked(self):
        if not self.vocabWidget.isEnabled():
            self.vocabWidget.setEnabled(True)
        if self.vocabWidget.isVisible():
            self.entriesListWidget.clear()

        params = {
            ':vocabName': self._getCurrentVocabName(),
        }

        entries = self.vocabEntriesManager.read(params)

        objects = [VocabEntry.from_dict(params).to_string()
                   for params in entries]

        self.vocabNameLabel.setText(params[':vocabName'])

        for obj in objects:
            item = QListWidgetItem(obj)
            item.setData(self.role, obj)
            self.entriesListWidget.addItem(item)

        self.vocabWidget.show()

    def onCreateVocabBtnClicked(self):
        dialog = VocabDialog(self)

        if dialog.exec() == QDialog.DialogCode.Accepted:
            params = dialog.params()

            result = self.vocabManager.create(params)

            if result:
                self._getVocabsList()

    def _getWordsAndTranslations(self) -> tuple[list[str], list[str]]:
        words: list[str] = list(
            map(lambda idx: self.entriesListWidget.item(idx).text().split(' -')[0],
                range(self.entriesListWidget.count()))
        )
        translations: list[str] = list(
            map(lambda idx: self.entriesListWidget.item(idx).text().split(' -')[1],
                range(self.entriesListWidget.count()))
        )

        return words, translations

    def _getVocabsList(self):
        self.vocabsListWidget.clear()
        names = self.vocabManager.readVocabularyNames()
        for name in names:
            item = QListWidgetItem(name)
            item.setData(self.role, name)
            self.vocabsListWidget.addItem(item)

    def _getCurrentVocabName(self) -> str:
        item = self.vocabsListWidget.currentItem()
        return item.data(self.role)


if __name__ == '__main__':
    app = QApplication()

    with open('ui/mainwindow/styles/main.qss', 'r') as file:
        qss = file.read()
    app.setStyleSheet(qss)

    w = MainWindow()

    sys.exit(app.exec())

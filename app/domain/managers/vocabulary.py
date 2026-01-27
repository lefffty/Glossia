from PySide6.QtSql import (
    QSqlQueryModel,
)

from .db import DatabaseManager


class VocabularyManager(QSqlQueryModel):
    def __init__(self, dbManager: DatabaseManager):
        self.dbManager = dbManager

    def create(self, params):
        sql = self.dbManager.config.insertVocabulary

        result = self.dbManager.executeQuery(sql, params, return_result=False)

        return result

    def delete(self, params: dict):
        sql1 = self.dbManager.config.deleteDictionary
        sql2 = self.dbManager.config.deleteDictionaryEntries

        _params = {
            ':vocabId': self._readVocabIdByName(params)[0]['vocab_id'],
        }

        self.dbManager.executeQuery(sql2, _params)

        return self.dbManager.executeQuery(sql1, _params)

    def readVocabularyNames(self):
        sql = self.dbManager.config.readDictionaries

        results = self.dbManager.executeQuery(sql, return_result=True)

        names = [result['name'] for result in results]

        return names

    def _readVocabIdByName(self, params):
        sql = self.dbManager.config.readVocabId

        return self.dbManager.executeQuery(sql, params, return_result=True)

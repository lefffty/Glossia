from .db import DatabaseManager


class WordTranslationManager:
    def __init__(self, dbManager: DatabaseManager, parent=None):
        self.dbManager = dbManager

    def createWord(self, params):
        sql = self.dbManager.config.insertWord

        self.dbManager.executeQuery(sql, params, return_result=False)

        return self._readWordIdByName(params)

    def createTranslation(self, params):
        sql = self.dbManager.config.insertTranslation

        self.dbManager.executeQuery(sql, params, return_result=False)

        return self._readTranslationIdByName(params)

    def _readWordIdByName(self, params: dict):
        sql = self.dbManager.config.readWordId

        return self.dbManager.executeQuery(sql, params, return_result=True)

    def _readTranslationIdByName(self, params: dict):
        sql = self.dbManager.config.readTranslationId

        return self.dbManager.executeQuery(sql, params, return_result=True)

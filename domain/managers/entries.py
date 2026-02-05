from .db import DatabaseManager
from .word import WordTranslationManager


class VocabularyEntriesManager:
    def __init__(self, dbManager: DatabaseManager, parent=None):
        self.dbManager = dbManager
        self.wordManager = WordTranslationManager(dbManager)

    def create(self, params: dict):
        sql = self.dbManager.config.insertDictionaryEntry

        vocabParams = {
            ':vocabName': params[':vocabId']
        }

        wordParams = {
            ':word': params[':wordId'],
        }

        translationParams = {
            ':translation': params[':translationId'],
        }

        vocabId = self._readVocabIdByName(vocabParams)[0]['vocab_id']

        wordId = self.wordManager._readWordIdByName(wordParams)

        if not wordId:
            wordId = self.wordManager.createWord(wordParams)
        else:
            wordId = self.wordManager._readWordIdByName(wordParams)
        wordId = wordId[0]['word_id']

        translationId = self.wordManager._readTranslationIdByName(
            translationParams)

        if not translationId:
            translationId = self.wordManager.createTranslation(
                translationParams)
        else:
            translationId = self.wordManager._readTranslationIdByName(
                translationParams)
        translationId = translationId[0]['translation_id']

        params = {
            ':vocabId': vocabId,
            ':wordId': wordId,
            ':translationId': translationId,
        }

        return self.dbManager.executeQuery(sql, params=params)

    def read(self, params: dict):
        sql = self.dbManager.config.readDictionaryWords

        vocab_id = self._readVocabIdByName(params)

        params = {
            ':vocabId': vocab_id[0]['vocab_id'],
        }

        return self.dbManager.executeQuery(sql, params, return_result=True)

    def delete(self, params):
        sql = self.dbManager.config.deleteDictionaryEntry

        wordParams = {
            ':word': params['word'],
        }
        wordId = self.wordManager._readWordIdByName(wordParams)[0]['word_id']

        translationParams = {
            ':translation': params['translation'],
        }
        translationId = self.wordManager._readTranslationIdByName(
            translationParams)[0]['translation_id']

        vocabParams = {
            ':vocabName': params['vocabName'],
        }
        vocabId = self._readVocabIdByName(vocabParams)[0]['vocab_id']

        params = {
            ':wordId': wordId,
            ':translationId': translationId,
            ':vocabId': vocabId,
        }

        return self.dbManager.executeQuery(sql, params=params)

    def _readVocabIdByName(self, params: dict):
        sql = self.dbManager.config.readVocabId

        return self.dbManager.executeQuery(sql, params, return_result=True)

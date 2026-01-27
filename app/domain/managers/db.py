from PySide6.QtSql import QSqlDatabase, QSqlQuery

from ..config.config import DatabaseConfig


class DatabaseManager:
    def __init__(self, config_path):
        self.config = DatabaseConfig(config_path)
        self._setupDatabase()
        self._initDatabase()

    def _setupDatabase(self):
        drivers = QSqlDatabase.drivers()

        if self.config.driver not in drivers:
            raise ValueError()

        self.db = QSqlDatabase.addDatabase(self.config.driver)
        self.db.setDatabaseName(self.config.path)

        if not self.db.open():
            raise ConnectionError(self.db.lastError().text())

    def _initDatabase(self):
        createVocabularyQuery = self.config.createVocabulary
        self.executeQuery(createVocabularyQuery)

        createWordQuery = self.config.createWord
        self.executeQuery(createWordQuery)

        createTranslationQuery = self.config.createTranslation
        self.executeQuery(createTranslationQuery)

        createTagQuery = self.config.createTag
        self.executeQuery(createTagQuery)

        createDictationQuery = self.config.createDictation
        self.executeQuery(createDictationQuery)

        createDictionaryEntryQuery = self.config.createDictionaryEntry
        self.executeQuery(createDictionaryEntryQuery)

        createDictionaryEntryTagQuery = self.config.createDictionaryEntryTag
        self.executeQuery(createDictionaryEntryTagQuery)

        createDictationEntryQuery = self.config.createDictationEntry
        self.executeQuery(createDictationEntryQuery)

    def _fetchResults(self, query: QSqlQuery):
        results = []
        while query.next():
            record = {}
            for i in range(query.record().count()):
                field_name = query.record().fieldName(i)
                record[field_name] = query.value(i)
            results.append(record)
        return results

    def executeQuery(self, sql, params: dict = None, return_result=False):
        query = QSqlQuery(self.db)

        if params:
            query.prepare(sql)
            if isinstance(params, dict):
                for key, value in params.items():
                    query.bindValue(key, value)
            else:
                for value in params:
                    query.addBindValue(value)
        else:
            query.prepare(sql)

        if not query.exec():
            raise ValueError

        if return_result:
            return self._fetchResults(query)
        return query

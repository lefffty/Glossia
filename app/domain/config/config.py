import yaml


class DatabaseConfig:
    def __init__(self, path):
        self._data = self._load_data(path)

    def _load_data(self, path):
        with open(path, 'r') as fp:
            return yaml.safe_load(fp)

    @property
    def path(self):
        return self._data['db']['path']

    @property
    def driver(self):
        return self._data['db']['driver']

    @property
    def createDictationEntry(self):
        script_path = self._data['db']['scripts']['createDictationEntry']
        with open(script_path, 'r') as fp:
            return fp.read()

    @property
    def createDictation(self):
        script_path = self._data['db']['scripts']['createDictation']
        with open(script_path, 'r') as fp:
            return fp.read()

    @property
    def createDictionaryEntry(self):
        script_path = self._data['db']['scripts']['createDictionaryEntry']
        with open(script_path, 'r') as fp:
            return fp.read()

    @property
    def createDictionaryEntryTag(self):
        script_path = self._data['db']['scripts']['createDictionaryEntryTag']
        with open(script_path, 'r') as fp:
            return fp.read()

    @property
    def createTag(self):
        script_path = self._data['db']['scripts']['createTag']
        with open(script_path, 'r') as fp:
            return fp.read()

    @property
    def createTranslation(self):
        script_path = self._data['db']['scripts']['createTranslation']
        with open(script_path, 'r') as fp:
            return fp.read()

    @property
    def createVocabulary(self):
        script_path = self._data['db']['scripts']['createVocabulary']
        with open(script_path, 'r') as fp:
            return fp.read()

    @property
    def createWord(self):
        script_path = self._data['db']['scripts']['createWord']
        with open(script_path, 'r') as fp:
            return fp.read()

    @property
    def insertDictionaryEntry(self):
        script_path = self._data['db']['scripts']['insertDictionaryEntry']
        with open(script_path, 'r') as fp:
            return fp.read()

    @property
    def insertDictionaryEntryTag(self):
        script_path = self._data['db']['scripts']['insertDictionaryEntryTag']
        with open(script_path, 'r') as fp:
            return fp.read()

    @property
    def insertDictationEntry(self):
        script_path = self._data['db']['scripts']['insertDictationEntry']
        with open(script_path, 'r') as fp:
            return fp.read()

    @property
    def insertVocabulary(self):
        script_path = self._data['db']['scripts']['insertVocabulary']
        with open(script_path, 'r') as fp:
            return fp.read()

    @property
    def insertWord(self):
        script_path = self._data['db']['scripts']['insertWord']
        with open(script_path, 'r') as fp:
            return fp.read()

    @property
    def insertTranslation(self):
        script_path = self._data['db']['scripts']['insertTranslation']
        with open(script_path, 'r') as fp:
            return fp.read()

    @property
    def insertTag(self):
        script_path = self._data['db']['scripts']['insertTag']
        with open(script_path, 'r') as fp:
            return fp.read()

    @property
    def insertDictation(self):
        script_path = self._data['db']['scripts']['insertDictation']
        with open(script_path, 'r') as fp:
            return fp.read()

    @property
    def readDictionaries(self):
        script_path = self._data['db']['scripts']['readDictionaries']
        with open(script_path, 'r') as fp:
            return fp.read()

    @property
    def readDictionaryWords(self):
        script_path = self._data['db']['scripts']['readDictionaryWords']
        with open(script_path, 'r') as fp:
            return fp.read()

    @property
    def readVocabId(self):
        script_path = self._data['db']['scripts']['readVocabId']
        with open(script_path, 'r') as fp:
            return fp.read()

    @property
    def readWordId(self):
        script_path = self._data['db']['scripts']['readWordId']
        with open(script_path, 'r') as fp:
            return fp.read()

    @property
    def readTranslationId(self):
        script_path = self._data['db']['scripts']['readTranslationId']
        with open(script_path, 'r') as fp:
            return fp.read()

    @property
    def deleteDictionary(self):
        script_path = self._data['db']['scripts']['deleteDictionary']
        with open(script_path, 'r') as fp:
            return fp.read()

    @property
    def deleteDictionaryEntry(self):
        script_path = self._data['db']['scripts']['deleteDictionaryEntry']
        with open(script_path, 'r') as fp:
            return fp.read()

    @property
    def deleteDictionaryEntries(self):
        script_path = self._data['db']['scripts']['deleteDictionaryEntries']
        with open(script_path, 'r') as fp:
            return fp.read()

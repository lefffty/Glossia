CREATE TABLE IF NOT EXISTS DictionaryEntry (
	entry_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	word_id INTEGER NOT NULL,
	translation_id INTEGER NOT NULL,
	vocab_id INTEGER NOT NULL,
	CONSTRAINT DictionaryEntry_Translation_FK FOREIGN KEY (translation_id) REFERENCES "Translation"(translation_id),
	CONSTRAINT DictionaryEntry_Vocabulary_FK FOREIGN KEY (vocab_id) REFERENCES Vocabulary(vocab_id),
	CONSTRAINT DictionaryEntry_Word_FK FOREIGN KEY (word_id) REFERENCES Word(word_id)
);
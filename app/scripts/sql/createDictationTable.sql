CREATE TABLE IF NOT EXISTS Dictation (
	dictation_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	vocab_id INTEGER NOT NULL,
	passed_at TEXT NOT NULL,
	CONSTRAINT Dictation_Vocabulary_FK FOREIGN KEY (vocab_id) REFERENCES Vocabulary(vocab_id)
);
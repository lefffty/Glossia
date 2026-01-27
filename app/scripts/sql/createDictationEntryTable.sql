CREATE TABLE IF NOT EXISTS DictationEntry (
	dictation_id INTEGER NOT NULL,
	entry_id INTEGER NOT NULL,
	word TEXT NOT NULL,
	"translation" TEXT NOT NULL,
	CONSTRAINT DictationEntry_PK PRIMARY KEY (dictation_id,entry_id),
	CONSTRAINT DictationEntry_Dictation_FK FOREIGN KEY (dictation_id) REFERENCES Dictation(dictation_id),
	CONSTRAINT DictationEntry_DictionaryEntry_FK FOREIGN KEY (entry_id) REFERENCES DictionaryEntry(entry_id)
);
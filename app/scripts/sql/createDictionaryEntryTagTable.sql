CREATE TABLE IF NOT EXISTS DictionaryEntryTag (
	tag_id INTEGER NOT NULL,
	entry_id INTEGER NOT NULL,
	CONSTRAINT DictionaryEntryTag_PK PRIMARY KEY (tag_id,entry_id),
	CONSTRAINT DictionaryEntryTag_DictionaryEntry_FK FOREIGN KEY (entry_id) REFERENCES DictionaryEntry(entry_id),
	CONSTRAINT DictionaryEntryTag_Tag_FK FOREIGN KEY (tag_id) REFERENCES Tag(tag_id)
);
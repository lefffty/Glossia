SELECT	
	de.entry_id AS entry_id,
	Word."text" AS word,
	t."text" AS translation
FROM DictionaryEntry de 
JOIN Word ON de.word_id = Word.word_id
JOIN "Translation" t ON de.translation_id = t.translation_id
WHERE de.vocab_id = :vocabId;
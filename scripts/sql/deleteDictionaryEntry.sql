DELETE FROM DictionaryEntry 
WHERE word_id = :wordId AND translation_id = :translationId AND vocab_id = :vocabId;
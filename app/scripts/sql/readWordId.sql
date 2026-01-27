SELECT
	w.word_id AS word_id
FROM Word w 
WHERE "text" = :word;
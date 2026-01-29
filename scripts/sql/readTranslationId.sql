SELECT
	t.translation_id AS translation_id
FROM "Translation" t 
WHERE t."text" = :translation;
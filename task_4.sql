"COLUMN_TYPE", "TABLE_SCHEMA = 'alx_book_store'", "TABLE_NAME = 'Books'"
SELECT COLUMN_NAME, DATA_TYPE, IS_NULLABLE, COLUMN_DEFAULT, CHARACTER_MAXIMUM_LENGTH, 
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'books'
AND TABLE_SCHEMA = DATABASE();
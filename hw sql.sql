-- Задание 1. Найти список CD и их цен, где название содержит только одно слово.
SELECT cdTitle, cdPrice
FROM CD
WHERE cdTitle NOT LIKE '% %';  -- Название не содержит пробела

-- Задание 2. Найти все CD и соответствующие имена исполнителей, где в названии есть строка "ro".
SELECT cdTitle, artName
FROM CD
JOIN Artist ON CD.artID = Artist.artID
WHERE cdTitle LIKE '%ro%';

-- Задание 3. Найти все записи из таблицы CD, где название содержит "he" на первом месте.
SELECT *
FROM CD
WHERE cdTitle LIKE 'he%';

-- и так далее...

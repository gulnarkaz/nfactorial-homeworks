-- Drop tables from previous exercises

DROP TABLE IF EXISTS Track;
DROP TABLE IF EXISTS CD;
DROP TABLE IF EXISTS Artist;

-- Create new tables

CREATE TABLE Artist (
       artID SERIAL NOT NULL,
       artName VARCHAR(255) NOT NULL,
       CONSTRAINT pk_artist PRIMARY KEY (artID),
       CONSTRAINT ck_artist UNIQUE (artName)
);

CREATE TABLE CD (
       cdID SERIAL NOT NULL,
       artID INT NOT NULL,
       cdTitle VARCHAR(255) NOT NULL,
       cdPrice REAL NOT NULL,
       cdGenre VARCHAR(255) NULL,
	cdNumTracks INT NULL,
       CONSTRAINT pk_cd PRIMARY KEY (cdID),
       CONSTRAINT fk_cd_art FOREIGN KEY (artID) REFERENCES Artist (artID)
);

-- Fill the tables up

-- Artist

INSERT INTO Artist (artName)
VALUES 	('Muse'),
		('Mr. Scruff'),
		('DeadMau5'),
		('Mark Ronson'),
		('Mark Ronson & The Business Intl'),
       	('Animal Collective'),
		('Kings of Leon'),
		('Maroon 5');

-- CD

INSERT INTO CD (artID, cdTitle, cdGenre, cdPrice) VALUES
((SELECT artID from Artist WHERE artName = 'Muse'), 'Black Holes and Revelations', 'Rock', 9.99),
((SELECT artID from Artist WHERE artName = 'Muse'), 'The Resistance', 'Rock', 11.99),
((SELECT artID from Artist WHERE artName = 'Mr. Scruff'), 'Ninja Tuna', 'Electronica', 9.99),
((SELECT artID from Artist WHERE artName = 'DeadMau5'), 'For Lack of a Better Name', 'Electro House', 9.99),
((SELECT artID from Artist WHERE artName = 'Mark Ronson'), 'Version', 'Pop', 12.99),
((SELECT artID from Artist WHERE artName = 'Mark Ronson & The Business Intl'), 'Record Collection', 'Alternative Rock', 11.99),
((SELECT artID from Artist WHERE artName = 'Animal Collective'), 'Merriweather Post Pavilion', 'Electronica', 12.99),
((SELECT artID from Artist WHERE artName = 'Kings of Leon'), 'Only By The Night', 'Rock', 9.99),
((SELECT artID from Artist WHERE artName = 'Kings of Leon'), 'Come Around Sundown', 'Rock', 12.99),
((SELECT artID from Artist WHERE artName = 'Maroon 5'), 'Hands All Over', 'Pop', 11.99);

/*
1.Find a list of CD titles and prices where the title contains exactly one word
2.Find all CD titles and the corresponding artist names where title contains the string “ro”
3.Find all the information from CD where title contains the letters “he” containing the single character at the beginning
4.Use a subquery to find a list of CDs that have the same genre as ‘Version’
5.Use IN to find a list of the titles of albums that are the same price as any ‘Electronica’ album
6.Use ANY to find the titles of CDs that cost less than at least one other CD
7.Use ALL to find a list of CD titles with the least price
8.Use EXISTS to find a list of Artists who produced a “Pop” CD
9.Find the names of Artists who have albums of “Rock” category. Provide at least two different queries producing the same solution
10.Find names of CDs produced by those Artists who have at least two words as their name
11.Find all information about CDs which are cheaper than others in the ‘Rock’ and ‘Pop’ categories only
12.Find the Artist names and their ID (in this order) for albums which cost £12.99. Provide three different queries producing the same solution
13.List the cd titles in reverse alphabetical order
14.List the titles, genres and prices of CDs in order of price from lowest to highest
15.List the titles, genres and prices of CDs in order of price from highest to lowest
16.List the titles, genres and prices of CDs in alphabetical order by genre, then by price from the highest price to the lowest one


17.Find a list of artist names, the number of CDs they have produced, and the average price for their CDs. Only return results for artists with more than one CD
18.Find a list of artist names, the number of CDs by that artist and the average price for their CDs but not including ‘Electronica’ albums (you might like to use a WHERE in this one too)
19.Find the difference between the average price of the rock albums and the average price of all albums excluding Muse’s CDs (ABS() will produce the absolute value of a calculation)
20.Find the artist name(s) with the most expensive CDs by average
21.Find the most expensive genre of music by calculating the minimum of the averages of all genres
22.Find a list of artist names, the number of CDs by that artist and the average price for their CDs but not including ‘Pop’ albums
*/

SELECT cdTitle, cdPrice
FROM CD
WHERE cdTitle NOT LIKE '% %'; 


SELECT cdTitle, artName
FROM CD
JOIN Artist ON CD.artID = Artist.artID
WHERE cdTitle LIKE '%ro%';

SELECT cdTitle, artName
FROM CD
JOIN Artist ON CD.artID = Artist.artID
WHERE cdTitle LIKE 'he%';

SELECT cdTitle, cdGenre
FROM CD
WHERE cdGenre = (SELECT cdGenre FROM CD WHERE cdTitle = 'Version');

SELECT cdTitle
FROM CD 
WHERE cdPrice IN (SELECT cdPrice FROM CD WHERE cdGenre = 'Electronica');

SELECT cdTitle
FROM CD
WHERE cdPrice < ANY (SELECT cdPrice FROM CD);

SELECT cdTitle
FROM CD   
WHERE cdPrice <= ALL (SELECT cdPrice FROM CD);

SELECT artName
FROM Artists 
WHERE EXISTS (
       SELECT 1 
       FROM CD 
       WHERE CD.artID = Artist.artID AND CD.cdGenre = 'Pop'
       );

SELECT artName
FROM Artist
WHERE artID IN (SELECT DISTINCT artID FROM CD WHERE cdGenre = 'Rock');

SELECT DISTINCT artName
FROM Artist
JOIN CD ON Artist.artID = CD.artID
WHERE cdGenre = 'Rock';

SELECT cdTitle
FROM CD
JOIN Artist ON CD.artID = Artist.artID
WHERE artName LIKE '% %';

SELECT *
FROM CD
WHERE cdGenre IN ('Pop', 'Rock') 
AND cdPrice < ALL (
       SELECT cdPrice 
       FROM CD 
       WHERE cdGenre IN ('Pop', 'Rock')
);

SELECT artName, artID
FROM Artist 
WHERE artID IN (
       SELECT artID 
       FROM CD 
       WHERE cdPrice = 12.99
       );

SELECT artName, artID
FROM Artist 
WHERE EXISTS (
       SELECT 1 
       FROM CD 
       WHERE CD.artID = Artist.artID 
       AND cdPrice = 12.99
       );

SELECT Artist.artName, Artist.artID
FROM Artist 
JOIN CD ON Artist.artID = CD.artID
WHERE CD.cdPrice = 12.99;

SELECT cdTitle 
FROM CD 
ORDER BY cdTitle DESC; 

SELECT cdTitle, cdGenre, cdPrice
FROM CD 
ORDER BY cdPrice ASC;

SELECT cdTitle, cdGenre, cdPrice
FROM CD 
ORDER BY cdPrice DESC;

SELECT cdTitle, cdGenre, cdPrice
FROM CD 
ORDER BY cdGenre ASC, cdPrice DESC;

SELECT Artist.artName, COUNT(CD.cdID) AS NumCDs, AVG(CD.cdPrice) AS avgPrice
FROM Artist 
JOIN CD ON Artist.artID = C.artID
GROUP BY Artist.artName D
HAVING COUNT(CD.cdID) > 1;


SELECT Artist.artName, COUNT(CD.cdID) AS NumCDs, AVG(CD.cdPrice) AS avgPrice
FROM Artist 
JOIN CD ON Artist.artID = CD.artID
WHERE CD.cdGenre <> 'Electronica'
GROUP BY Artist.artName;

SELECT ABS(
       (SELECT AVG(cdPrice) FROM CD WHERE cdGenre = 'Rock') -
       (SELECT AVG(cdPrice) FROM CD WHERE artID <> (SELECT artID FROM Artist WHERE artName = 'Muse'))
) AS priceDifference;

SELECT artName
FROM Artist 
JOIN CD ON Artist.artID = CD.artID
GROUP BY artName
ORDER BY AVG(cdPrice) DESC
LIMIT 1;

SELECT cdGenre
FROM CD 
GROUP BY cdGenre 
ORDER BY MIN(cdPrice) DESC 
LIMIT 1;

SELECT Artist.artName, COUNT(CD.cdID) AS NumCDs, AVG(CD.cdPrice) AS avgPrice
FROM Artist 
JOIN CD ON Artist.artID = CD.artID
WHERE CD.cdGenre <> 'Pop'
GROUP BY Artist.artName;

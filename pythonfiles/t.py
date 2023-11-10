print("a")
print("b")
print("c")
print("d")
print("e")
print("f")
print("g")
print("h")
print("i")
print("j")

***
--SELECT first_name,last_name FROM customer WHERE first_name LIKE 'Jen%';
--SELECT first_name,last_name FROM customer WHERE last_name LIKE 'J%';
--SELECT COUNT(amount) FROM payment WHERE amount>5;
--SELECT COUNT(DISTINCT(district)) FROM address;
--SELECT DISTINCT(district) FROM address;
--SELECT COUNT(*) FROM film WHERE title LIKE '%Truman%';
--SELECT COUNT(customer_id) FROM customer GROUP BY email;
--SELECT * FROM customer;
--SELECT COUNT(amount),staff_id,SUM(amount)FROM payment GROUP BY staff_id;
--SELECT COUNT(amount),staff_id,SUM(amount)FROM payment GROUP BY staff_id;
--SELECT COUNT(amount),staff_id,SUM(amount)FROM payment GROUP BY staff_id;
--SELECT COUNT(customer_id),store_id FROM customer GROUP BY store_id HAVING COUNT(customer_id)>5;
--SELECT COUNT(customer_id),store_id FROM customer GROUP BY store_id HAVING COUNT(customer_id)>5;
--SELECT customer_id,count(amount) FROM payment GROUP BY customer_id HAVING COUNT(amount)>35 ORDER BY COUNT(amount) DESC;
--SELECT * FROM customer
--SELECT * FROM payment
--SELECT * FROM customer INNER JOIN payment ON customer.customer_id = payment.customer_id
--SELECT * FROM customer INNER JOIN payment ON payment.customer_id
--SELECT City FROM customer UNION 
--CREATE TABLE weblinks(ID serial PRIMARY KEY, url VARCHAR(255) NOT null, name VARCHAR(255) NOT null, description VARCHAR(255));
--SELECT * FROM weblinks
--INSERT INTO weblinks(url,name) VALUES('www.Amazon.com','Amazon'),('www.ign.com','IGN'),('www.cuny.edu','CUNY');
--CREATE TABLE copy_table(LIKE weblinks);
--SELECT * FROM copy_table
--UPDATE weblinks SET description='Website for all your shopping needs' WHERE name LIKE 'Amazon%'
--SELECT * FROM weblinks
***





***
--CREATE TABLE videos (ID serial PRIMARY KEY, title VARCHAR(255) NOT null, length VARCHAR(255) NOT null, URL VARCHAR(255) NOT null);
--INSERT INTO videos VALUES(1,'How to Make a Landing Page using HTML, SCSS, and JavaScript','5:05:00','https://www.youtube.com/watch?v=aoQ6S1a32j8&feature=youtu.be'),
--(2,'How to Design a Website – A UX Wireframe Tutorial','30:00','https://www.youtube.com/watch?v=pN92rnO_n5U'),(3,'Legend of Atlantis (Full Episode) | Drain the Oceans','47:22','https://www.youtube.com/watch?v=ErPsyBUCijM')
--SELECT*FROM videos
--CREATE TABLE Reviewers (name VARCHAR(255) PRIMARY KEY, title VARCHAR(255) NOT null, rating integer, text VARCHAR(255) NOT null);
--INSERT INTO Reviewers VALUES('John','How to Make a Landing Page using HTML, SCSS, and JavaScript','4','It is useful!'),('Asher','Legend of Atlantis (Full Episode) | Drain the Oceans','5','Love it!'),('Ethan','The Buried Mysteries Of Angkor Wat | The City Of God Kings | Timeline','3','Good!')
--SELECT*FROM Reviewers
--INSERT INTO Reviewers VALUES('Ethan','The Buried Mysteries Of Angkor Wat | The City Of God Kings | Timeline','3','Good!')
SELECT * FROM videos FULL OUTER JOIN Reviewers ON videos.title=Reviewers.title

***
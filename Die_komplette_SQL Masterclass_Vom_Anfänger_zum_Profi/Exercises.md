# V23: 1. Exercise - 'baby_names'
### (1) Wie viele Einträge gibt es insgesamt in der Tabelle baby_names?

	SELECT COUNT(*) FROM baby_names

### (2)  Wie viele männliche Personen (gender = M) wurden im Jahr 2010 geboren, die „Alex“ heißen?

	SELECT COUNT(*) FROM baby_names WHERE 
		("name" = 'Alex' AND "gender" = 'M' AND "year" = 2010)

### (3) Wie viele unterschiedliche Namen gibt es in unserer Tabelle… wenn:
#### (3-1) Das Geschlecht egal ist (d.h. "Alex" für das Geschlecht M und "Alex" für das Geschlecht "F" zählt als der gleiche Name)

	SELECT COUNT(DISTINCT("name")) FROM baby_names 

#### (3-2) Das Geschlecht nicht egal ist (d.h. "Alex" für das Geschlecht M und "Alex" für das Geschlecht "F" zählen als 2 unterschiedliche Namen)

	SELECT COUNT(DISTINCT("name", "gender")) FROM baby_names 

### (4) Welcher Baby-Name wurde in einem bestimmten Jahr exakt 19250 mal vergeben?

	SELECT * FROM baby_names WHERE count = 19250

### (5) Gibt es das Geschlecht „divers“ in unserer Tabelle? Kannst du das mit den dir bisher bekannten Befehlen herausfinden?

	SELECT DISTINCT("gender") FROM baby_names   

# V32: 2. Exercise - 'baby_names'
### (1) Wie viele unterschiedliche Vornamen gibt es, die mit „Alex“ anfangen, „Alex“ eingeschlossen? Hierbei spielt das Geschlecht keine Rolle.

	SELECT COUNT(DISTINCT("name")) FROM baby_names WHERE "name" LIKE 'Alex%' # -> 20 

### (2) Wie viele unterschiedliche Vornamen gibt es, in denen im Vornamen ein „m“ enthalten ist? Das „m“ darf auch an erster Stelle stehen.  

	SELECT COUNT(DISTINCT("name")) FROM baby_names WHERE "name" LIKE '%m%' OR "name" LIKE 'M%' # -> 1183	

### (3) Wie viele Zeilen gibt es in der Tabelle, bei denen das Jahr im 20. Jahrhundert (1900 bis einschließlich 1999) ist? 
Einmal mit BETWEEN einmal ohne

	SELECT COUNT("year") FROM baby_names WHERE "year" BETWEEN 1900 AND 1999      # -> 100
	SELECT COUNT("year") FROM baby_names WHERE "year" >= 1900 AND "year" <= 1999 # -> 100

### (4) Wie viele Zeilen gibt es in der Tabelle, bei denen das Jahr im 20. Jahrhundert (1900 bis einschließlich 1999) ist, und durch 10 Teilbar ist?

Löse diese Aufgabe mit vielen ORs

	SELECT COUNT("year") FROM baby_names WHERE 
		"year" = 1900 OR "year" = 1910 OR "year" = 1920 OR "year" = 1930 OR
	    "year" = 1940 OR "year" = 1950 OR "year" = 1960 OR "year" = 1970 OR
	    "year" = 1980 OR "year" = 1990 # -> 15307

Löse diese Aufgabe mit einem WHERE IN()

	SELECT COUNT("year") FROM baby_names WHERE 
		"year" IN (1990, 1980, 1970, 1960, 1950, 1940, 1930, 1920, 1910, 1900) # -> 15307

Löse die Aufgabe mit einem LIKE

	SELECT COUNT("year") FROM baby_names WHERE year::varchar LIKE '19_0'       # -> 15307

Löse diese Aufgabe mit einem Modulo

	SELECT COUNT("year") FROM baby_names WHERE 								   # -> 15307
		"year"%10 = 0 AND year BETWEEN 1900 AND 1999

# V41: 3. Exercise - 'baby_names'
### (1) Welcher Vorname kam insgesamt (d.h. für ein beliebiges Geschlecht in einem beliebigen Jahr) am häufigsten vor?

	SELECT * FROM baby_names ORDER BY "count" DESC LIMIT 3 # -> Linda

### (2) Welches Jahr ist das erste Jahr in unserer Datenbasis?
Löse dies mit Hilfe der MIN()-Funktion

	SELECT MIN("year") FROM baby_names # -> 1880

Löse dies ohne die MIN()-Funktion

	SELECT DISTINCT("year") FROM baby_names ORDER BY "year" LIMIT 5  # -> 1880

### (3) Wie viele unterschiedliche Vornamen gibt es, die aus exakt 5 Buchstaben bestehen?
Löse dies mit einem WHERE und der LENGTH()-Funktion

	SELECT COUNT(DISTINCT("name")) FROM baby_names WHERE LENGTH("name") = 5  # -> 1590

Löse dies mit einem WHERE und einem LIKE (hier gab es einen speziellen Platzhalter)

	SELECT COUNT(DISTINCT("name")) FROM baby_names WHERE "name" LIKE '_____' # -> 1590

### (4) Wie viele Babys sind für das Jahr 2000 insgesamt in unserer Datenbasis? Berechne hier die Summe aller Einträge!

	SELECT SUM(count) FROM baby_names WHERE year = 2020 # -> 3.320.671

### (5) Wenn wir alle unterschiedlichen Vornamen betrachten (Geschlecht ist egal), und aufsteigend alphabetisch sortieren - Welcher Vorname steht auf der 2. Seite ganz oben, wenn die erste Seite aus 10 Einträgen besteht?

	SELECT DISTINCT("name") FROM baby_names ORDER BY "name" OFFSET 10 LIMIT 1 # -> Aarna

# V54: 4. Exercise - 'locations'
### (1) Leider hat sich in diesen Daten ein kleiner Fehler eingeschlichen. Die Adresse der „Buchhandlung DOM“ ist das Domkloster 4 und nicht das Domkloster 1. Aktualisiere daher die Daten mit einem UPDATE-Befehl.
Hinweis 1: Beachte hierbei, dass die Stadt und die Postleitzahl erhalten bleibt.  
Hinweis 2: Genau aus diesem Grund speichert man die Adresse oft aufgeteilt in verschiedenen Feldern in der Datenbank, d.h. 1 Feld für die Straße, eins für die Stadt, eins für die Postleitzahl,…

	UPDATE locations SET address = 'Domkloster 4, 50667 Köln' WHERE address = 'Domkloster 1, 50667 Köln' 

### (2) Die Buchhandlung Alexanderplatz musste Anfang dieses Monats geschlossen werde. Entferne sie daher aus der Datenbank!

	DELETE FROM locations WHERE id = 2

### (3) Eine neue Buchhandlung soll nach nur 20 Jahren Bauzeit noch diesen Monat in Berlin eröffnet werden. Füge daher folgenden Eintrag in die Datenbank ein:
Titel: Buchhandlung Flughafen BER & Adresse: Melli-Beese-Ring 1, 12529 Schönefeld, Deutschland

	INSERT INTO locations ("title", "address") VALUES ('Buchhandlung Flughafen BER', 'Melli-Beese-Ring 1, 12529 Schönefeld, Deutschland')

# V79: 5. Exercise Tabellen verwalten
### (1) Erstelle eine Tabelle („newsletter“), in der wir die Registrierungen für einen Newsletter abspeichern können.
Wir benötigen folgende Spalten:
ID  
E-Mail-Adresse vom Kunden (zwingend benötigt)  
Name vom Kunden (optional)  
Alter in Jahren (optional)  

		CREATE TABLE newsletter (
		    ID SERIAL PRIMARY KEY,
		    EMail VARCHAR(1000) NOT NULL,
		    Name VARCHAR(1000),
		    Alter INTEGER
		)

### (2) Tabellen abändern
Füge anschließend folgende Spalte zu der Tabelle noch hinzu: 
- Datenschutzvereinbarung akzeptiert: Datentyp: BOOLEAN Standardmäßig ausgefüllt mit FALSE

		ALTER TABLE newsletter 
			ADD COLUMN Datenschutz BOOLEAN NOT NULL DEFAULT FALSE

# V97 6. Exercise SUBSELECTS - Versuche, alle Aufgaben jeweils mit exakt einer Query zu lösen!
Betrachte die Tabelle books. In der Spalte „language“ ist die jeweilige Sprache von einem jeden Buch notiert.

### (1) Wie viel % der Bücher sind in deutscher Sprache? Versuche dies mit einer Query zu lösen!
Tipp 1: Mit einem SELECT (SUBQUERY), (SUBQUERY) kannst du 2 komplett unterschiedliche Subqueries an die Datenbank schicken, sofern sie jeweils nur einen Wert aggregieren (z.B. die Anzahl ermitteln,…). Es wird hier nicht zwingend die Angabe einer Tabelle benötigt! <br/>
Tipp 2: Auch kannst du die Ergebnisse direkt miteinander verrechnen: SELECT (SUBQUERY) / (SUBQUERY). Wichtig: Funktioniert so nur in MySQL, unter PostgreSQL gibt es noch was zu beachten – siehe Musterlösung.

	SELECT
		(SELECT COUNT(*) from books WHERE language = 'de')::float /  / # Amount of german books
		(SELECT COUNT(*) from books)::float /                          # Amount of all books


### (2) Erstelle eine Auflistung aller Bücher inkl. dem jeweiligen Thema!
Betrachte die Tabelle books. Jedes Buch hat ein Thema / eine Kategorie, die entsprechende Information hierzu findet sich in der Tabelle books_subjects. 

	SELECT title, 
	    (SELECT title FROM books_subjects 
	        	WHERE books.subject_id = books_subjects.id) AS Category
	FROM books

### (3) Zu welchem Thema gibt es am meisten Bücher, und wie viele Bücher sind das? 
Betrachte die Tabelle books_subjects, ein Thema kann von mehreren Büchern verwendet werden. Wie oft kommt das beliebteste Thema vor? 

	SELECT title,
	    (SELECT COUNT(*) FROM books 
	            WHERE books.subject_id = books_subjects.id) AS topic_freq
	FROM books_subjects ORDER BY topic_freq DESC

### (4) Betrachte die Tabelle books. Welcher Autor hat bisher am meisten Bücher veröffentlicht?
Tipp 1: Ermittle also zuerst alle unterschiedlichen Autoren, die es in der Tabelle gibt <br/> 
Tipp 2: Erweitere anschließend die Query, sodass für jeden gefundenen Autor eine Subquery gestartet wird, die zu diesem Autor die entsprechende Anzahl an Büchern ermittelt <br/>
Tipp 3: Beachte hierbei, dass hier das Subselect 2x auf der gleichen Tabelle ausgeführt wird – hier wirst du die Tabellen also u.U. mit einem AS benennen müssen! <br/> 

Hinweis: Das würde mit einem GROUP BY sehr viel effizienter gehen – das haben wir uns aber noch nicht angeschaut…

		SELECT DISTINCT(creator),
		    (SELECT COUNT(*) FROM books AS books_new 
		            WHERE books_new.creator = books_old.creator) AS amount_books
		FROM books AS books_old ORDER BY amount_books DESC

# V109 7. Exercise JOINS
Hinweis: Diese Aufgaben ähneln sich u.U. den Aufgaben zum Abschnitt „Subselect“ – sie sind aber unterschiedlich!

### (1) Betrachte die Tabelle books. 
Jedes Buch hat ein Thema / eine Kategorie (Spalte: subject_id), die entsprechende Information hierzu findet sich in der Tabelle books_subjects.

#### 1.1 Erstelle eine Auflistung aus Büchern sowie den entsprechenden Themen, verwende hierzu einen JOIN
		SELECT * FROM books
		    LEFT JOIN books_subjects ON books.id = books_subjects.id

#### 1.2 Es gibt Bücher, bei denen die Spalte subject_id auf NULL gesetzt ist. 
Wenn du ein SELECT auf der Tabelle „books“ ausführst, und die Tabelle „books_subjects“ per JOIN vernüpfst – welcher/welche JOIN-Typ(en) sorgt dafür, dass alle Bücher übersprungen werden,  wo die Spalte subject_id NULL ist?

		SELECT * FROM books
    		LEFT JOIN books_subjects ON books.subject_id = books_subjects.id

#### 1.3 Wie viele deutschsprachige Liebesgeschichten (Thema: „Love stories“) gibt es? 
Löse diese Frage – sofern möglich - mit einer einzigen Datenbankabfrage, ohne zuvor die ID des Themas „Love stories“ zu ermitteln!

		SELECT COUNT(*) FROM books
		    LEFT JOIN books_subjects ON books.subject_id = books_subjects.id
		    WHERE books.language = 'de' 
		    AND books_subjects.title LIKE '%Love stories%'

# V120 7. Exercise GROUP BY

### (1) In der Tabelle „baby_names“ finden sich Geburtsstatistiken aus den USA. 

#### 1.1 Welcher Vorname wurde insgesamt am häufigsten vergeben? Das Geschlecht spielt hierbei keine Rolle
		SELECT name, SUM(count) FROM baby_names
		    GROUP BY name 
		    ORDER BY SUM(count) DESC

#### 1.2 Welcher Vorname wurde im Jahr 1950 am häufigsten vergeben? Das Geschlecht spielt hierbei keine Rolle
		SELECT name, count FROM baby_names
		    WHERE year = 1950
		    GROUP BY name, count
		    ORDER BY count DESC 

#### 1.3 Erstelle eine Auflistung von allen Vornamen, welche insgesamt mehr als 5 Millionen mal vergeben wurden. 
Versuche, diese Auflistung mit nur einer Query zu generieren. Wie viele Einträge erscheinen hier in der Auflistung?

		SELECT name, SUM(count) FROM baby_names
		    GROUP BY name 
		    HAVING SUM(count) > 5000000
		    ORDER BY SUM(count) DESC

#### 1.4 In welchem Jahr wurden am meisten verschiedene Vornamen vergeben?
		SELECT year, COUNT(DISTINCT(name)) FROM baby_names
		    GROUP BY year
		    ORDER BY COUNT(DISTINCT(name)) DESC

#### 1.5 Gibt es insgesamt mehr weibliche oder mehr männliche Babys in der Statistik?
 
		SELECT gender, SUM(count) FROM baby_names
		    GROUP BY gender
		    ORDER BY SUM(count) DESC

### 1.6 Mit welchem Buchstaben begann im Jahr 2010 der Name der meisten Babys? 
Den ersten Buchstaben kannst du über SUBSTR(spalte, 1, 1) ermitteln.

		SELECT SUBSTR(name, 1, 1), SUM(count) FROM baby_names
		    WHERE year = 2010
		    GROUP BY SUBSTR(name, 1, 1)
		    ORDER BY COUNT(*) DESC

#### 1.7 Bonus (nicht zwingend GROUP BY): Wie viele Vornamen aus dem Jahr 1880 gibt es im Jahr 2010 nicht mehr?  

		SELECT name FROM baby_names
		    WHERE year = 1880 AND
		    (SELECT COUNT(*) FROM baby_names as b2 WHERE b2.name = baby_names.name AND b2.year = 2010) = 0

### (2) Betrachte die Tabelle „books“, in dieser sind diverse Daten zu Büchern gespeichert. 
Fast jedes Buch hat ein verknüpftes Thema (Spalte: subject_id), dieses Thema wird in der Tabelle „books_subjects“ abgespeichert.

#### 2.1 Zu welchem Thema gibt es am meisten Bücher? Löse diese Frage mit einem JOIN + GROUP BY

		SELECT books_subjects.title, COUNT(books_subjects.title) FROM books
		    LEFT JOIN books_subjects ON books.subject_id = books_subjects.id
		    GROUP BY books_subjects.title
		    ORDER BY COUNT(books_subjects.title) DESC # --> 1.750 Fiction

#### 2.2 Welcher Autor hat am meisten Liebesromane (books_subjects.title = 'Love stories') geschrieben? 
Löse diese Frage mit einem JOIN + GROUP BY

		SELECT books.creator, COUNT(books.creator) FROM books
		    LEFT JOIN books_subjects ON books.subject_id = books_subjects.id
		    WHERE books_subjects.title LIKE '%Love stories%'
		    GROUP BY books.creator 
		    ORDER BY COUNT(books.creator) DESC # --> Bar Amelia & Bacon Josephine: 5x LoveStories

#### 2.3 Welcher Autor hat am meisten Downloads? 
Beachte, dass ein Autor mehrere Bücher haben kann, die entsprechenden Downloads müssen aufsummiert werden <br/>
 Wichtig: „Various“, NULL, Anonymous,… zählen hierbei nicht als Autor

		SELECT books.creator, SUM(books.downloads) FROM books
		    GROUP BY books.creator 
		    ORDER BY SUM(books.downloads) DESC # --> Austen, Jane: 44.177x

#### 2.4 Schreibe eine Query, die alle Autoren ausgibt, die mehr als 30.000 Downloads mit ihren Büchern erreicht haben. 
Frage: Wie viele Autoren sind in dieser Auflistung enthalten? - Wichtig: „Various“, NULL, Anonymous,… zählen hierbei nicht als Autor

		SELECT books.creator, SUM(books.downloads) FROM books
		    GROUP BY books.creator 
		    HAVING SUM(books.downloads) > 30000
		    ORDER BY SUM(books.downloads) DESC # --> 4 authors

#### 2.5 Wir möchten ein neues Buch veröffentlichen, dieses soll sich aber so gut wie möglich verkaufen. 
In welcher Sprache sollten wir dieses Buch schreiben? Bzw. anders ausgedrückt: Für welche Sprache gibt es aktuell durchschnittlich die meisten Downloads pro Buch?

		SELECT language, SUM(books.downloads) / COUNT(*) FROM books
		    GROUP BY books.language 
		    ORDER BY SUM(books.downloads) / COUNT(*) DESC #--> KO 455 sales per book

# 135 8. Exercise DATUMSWERTE
# Betrachte die Tabelle „books“, in dieser sind diverse Daten zu Büchern gespeichert.
# 	  1.1 Wie viele Bücher wurden im Jahr 2005 herausgegeben?
		SELECT COUNT(*) FROM books
		    WHERE DATE_PART('year', issued) = '2005'

#  	  1.2 Betrachte die Spalte „issued“. In welchem Monat werden im Schnitt am meisten neue Bücher herausgegeben?
		SELECT DATE_PART('month', issued), COUNT(*) AS counts FROM books
		    GROUP BY DATE_PART('month', issued)
		    ORDER BY counts DESC

#	  1.3 Schwer: Welcher Autor war am längsten aktiv? Anders ausgedrückt: 
#         Bei welchem Autor ist die Zeitdifferenz zwischen dem Herausgabedatum seines ersten Buches und seines letzten Buches am größten?
		SELECT creator, MIN(issued), MAX(issued), MAX(issued) - MIN(issued) AS DIFF from books
		    GROUP BY creator
		    ORDER BY DIFF DESC

# 149 9. Exercise INDEXE
# Betrachte die Tabelle „baby_names“.
# Sortiere die Tabelle nach dem Namen. 
		SELECT * FROM baby_names
    		ORDER BY name ASC # --> 00:00:01.493

# Wie lange dauert dies im Vergleich zu einer Sortierung nach einer anderen Spalte? 
		SELECT * FROM baby_names
    		ORDER BY year ASC # --> 00:00:01.392

    	SELECT * FROM baby_names
    		ORDER BY gender ASC # --> 00:00:01.302

    	SELECT * FROM baby_names
    		ORDER BY id ASC # --> 00:00:01.669

    	SELECT * FROM baby_names
    		ORDER BY count ASC # --> 00:00:01.210

# Wie könntest du diese Sortierung beschleunigen?
		CREATE INDEX name_id ON baby_names (
    		name ASC
		)

		SELECT * FROM baby_names
		    ORDER BY name ASC # --> 00:00:00.782

		# OBACHT 
		SELECT * FROM baby_names
    		ORDER BY name DESC # --> 00:00:02.167 -> andere Ordnung als IDX -> langsamer


# 202 10. Exercise FUNCTIONS
# Schreibe eine Funktion, die - anhand einer ID - einen einzelnen Kunden von customers zurück gibt 
# & tracked wann welche ID angefragt wurde.
# (1) Erstelle eine 'Logg'-Tabelle, um die Daten zu speichern
CREATE TABLE loggs (
    ID SERIAL PRIMARY KEY,
    time_stamp TIMESTAMP WITH TIME ZONE,
    queried_ID BIGINT
)

# (2) Erstelle eine Funktion, die anhand der ID einen customers-Eintrag zurück gibt &
#     die Anfrage, sowie die angefragte ID loggt
CREATE FUNCTION customer_info_w_logg(bigint) RETURNS table(id bigint, email varchar, name_full varchar) AS $$
    INSERT INTO loggs("time_stamp", "queried_id") VALUES(CURRENT_TIMESTAMP, $1);
    SELECT id, email, concat(firstname, lastname) FROM customers
        WHERE ID = $1
    $$ LANGUAGE SQL

# (3) Erstelle eine Anfrage & vergleich die Ergebnisse + check ob es gelogged wurde
# 3-1) Orginal ID
SELECT id, email, concat(firstname, lastname) FROM customers
    WHERE ID = 23

# 3-2) Original loggs
SELECT * FROM loggs

# 3-3) Run the request + check the loggs table
SELECT * FROM customer_info_w_logg(23)
SELECT * FROM loggs

# 237 11. Exercise TRIGGER
# 'customers' hat alle Kunden & für eine Anwendung brauchen wir für jeden Kunden den gesamtem Umsatz 
# - füge dies als extra Spalte zu 'customers' hinzu (Umsatz berechnet sich über 'amount' in 'orders'
#     --> Löse dieses Problem über verschiedene Wege
# (1) Über einen normal VIEW lösen
CREATE VIEW customers_spent_1 AS 
SELECT *,
    (SELECT SUM(amount) FROM orders WHERE customers.id = orders.customer_id) AS Totally_Spent
    FROM customers

SELECT * FROM customers_spent_1

# (2) Über einen materialized VIEW
CREATE MATERIALIZED VIEW customers_spent AS 
    SELECT *, 
        (SELECT SUM(amount) FROM orders WHERE customers.id = orders.customer_id) AS Totally_Spent
    FROM customers
    
SELECT * FROM customers_spent

# (3) Über einen Trigger - neue Spalte erstellen & immer updaten, wenn sich was bei 'orders' ändert
#   Add a column 'spent_all' to customers 
ALTER TABLE customers
    ADD COLUMN spent_all DECIMAL(10, 2)
    
#   Fill the values to 'spent_all' */
UPDATE customers 
    SET spent_all = (SELECT SUM(amount) FROM orders 
                        WHERE orders.customer_id = customers.id)
    
#   Delete triggers, so we can run the code again 
DROP TRIGGER IF EXISTS orders_after_insert_trigger ON orders;
DROP FUNCTION IF EXISTS orders_after_insert();

#   Write a Trigger-Function for when something is inserted in orders
CREATE FUNCTION orders_after_insert() # -> Must not take any arguments 
    RETURNS TRIGGER
    LANGUAGE 'plpgsql'
    VOLATILE AS $CODE$ BEGIN
        UPDATE customers SET spent_all = 
            (SELECT SUM(amount) FROM orders 
                WHERE orders.customer_id = customers.id)
                WHERE customers.id = NEW.customer_id;
        RETURN NEW;
    END $CODE$;
    
# 	Write the trigger itself */
CREATE TRIGGER orders_after_insert_trigger
    AFTER INSERT ON orders
    FOR EACH ROW EXECUTE PROCEDURE orders_after_insert();

#	Check the Trigger-Function */
SELECT * FROM customers WHERE ID = 1
SELECT * FROM orders WHERE customer_id = 1

INSERT INTO orders (timestamp, amount, customer_id) 
    VALUES (CURRENT_TIMESTAMP, 100, 1)
    
SELECT * FROM customers WHERE ID = 1 /* Has been updated now! */


#	Delete triggers, so we can run the code again */
DROP TRIGGER IF EXISTS orders_after_delete_trigger ON orders;
DROP FUNCTION IF EXISTS orders_after_delete();

#	Write a Trigger-Function for when something is deleted in orders */
CREATE FUNCTION orders_after_delete() /* Must not take any arguments */ 
    RETURNS TRIGGER
    LANGUAGE 'plpgsql'
    VOLATILE AS $CODE$ BEGIN
        UPDATE customers SET spent_all = 
            (SELECT SUM(amount) FROM orders 
                WHERE orders.customer_id = customers.id)
                WHERE customers.id = OLD.customer_id;
        RETURN NEW;
    END $CODE$;
    
#	Write the trigger itself */
CREATE TRIGGER orders_after_delete_trigger
    AFTER DELETE ON orders
    FOR EACH ROW EXECUTE PROCEDURE orders_after_delete();
    
#	Check the Trigger-Function */
SELECT * FROM customers WHERE ID = 1
SELECT * FROM orders WHERE customer_id = 1

DELETE FROM orders WHERE id = 1053
    
SELECT * FROM customers WHERE ID = 1
SELECT * FROM orders WHERE customer_id = 1 /* Has been updated now! */


#	Delete triggers, so we can run the code again */
DROP TRIGGER IF EXISTS orders_after_update_trigger ON orders;
DROP FUNCTION IF EXISTS orders_after_update();

#	Write a Trigger-Function for when something is deleted in orders */
CREATE FUNCTION orders_after_update() /* Must not take any arguments */ 
    RETURNS TRIGGER
    LANGUAGE 'plpgsql'
    VOLATILE AS $CODE$ BEGIN
        UPDATE customers SET spent_all = 
            (SELECT SUM(amount) FROM orders 
                WHERE orders.customer_id = customers.id)
                WHERE customers.id = NEW.customer_id OR
                      customers.id = OLD.customer_id;
        RETURN NEW;
    END $CODE$;
    
#	Write the trigger itself */
CREATE TRIGGER orders_after_update_trigger
    AFTER UPDATE ON orders
    FOR EACH ROW EXECUTE PROCEDURE orders_after_update();
    
#	Check the Trigger-Function */
SELECT * FROM customers WHERE ID = 1
SELECT * FROM orders WHERE customer_id = 1

UPDATE orders SET amount = 100 WHERE customer_id = 1 

SELECT * FROM orders WHERE customer_id = 1 
SELECT * FROM customers WHERE ID = 1 /* Both has been updated now! */

SELECT * FROM customers WHERE ID in (1, 2)
UPDATE orders SET customer_id = 2 WHERE customer_id = 1
SELECT * FROM orders WHERE customer_id in (1,2)
SELECT * FROM customers WHERE ID in (1, 2) /* Both has been updated now! */


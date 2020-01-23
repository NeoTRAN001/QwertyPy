CREATE TABLE Distro (
	id INTEGER PRIMARY KEY,
	distro_name VARCHAR(30),
	kernel VARCHAR(30),
	de_id INT
);

CREATE TABLE DE (
	id INTEGER PRIMARY KEY,
	de_name VARCHAR(10)
);

SELECT * FROM DE;
SELECT * FROM Distro;

INSERT INTO DE (id, de_name) 
	VALUES (1, 'KDE'), (2, 'XFCE');

INSERT INTO Distro (id, distro_name, kernel, de_id)
	VALUES (1, 'MX Linux', '4.19', 2);

SELECT D.id, D.distro_name, D.kernel, DE.de_name FROM Distro AS D
	INNER JOIN DE ON D.de_id = DE.id;



CREATE TABLE Movie(
	id INT NOT NULL, 
	title VARCHAR(100) NOT NULL, 
	year INT, 
	rating VARCHAR(10), 
	company VARCHAR(50),
	PRIMARY KEY(id)
);

CREATE TABLE Actor(
	id INT NOT NULL, 
	last VARCHAR(20), 
	first VARCHAR(20), 
	sex VARCHAR(6), 
	dob DATE,
	dod DATE,
	PRIMARY KEY(id),
	CHECK (DATEDIFF(dob, dod) >= 0) /* Date of birth should smaller than the date of death */
);

CREATE TABLE Director(
	id INT NOT NULL, 
	last VARCHAR(20), 
	first VARCHAR(20), 
	sex VARCHAR(6), 
	dob DATE,
	dod DATE,
	PRIMARY KEY(id),
	CHECK (DATEDIFF(dob, dod) >= 0)
);

CREATE TABLE MovieGenre(
	mid INT NOT NULL, 
	genre VARCHAR(20), 
	FOREIGN KEY(mid) references Movie(id)
);

CREATE TABLE MovieDirector(
	mid INT NOT NULL, 
	did INT NOT NULL,
	FOREIGN KEY(mid) references Movie(id),
	FOREIGN KEY(did) references Director(id)
);

CREATE TABLE MovieActor(
	mid INT NOT NULL, 
	aid INT NOT NULL,
	role VARCHAR(50) NOT NULL,
	FOREIGN KEY(mid) references Movie(id),
	FOREIGN KEY(aid) references Actor(id)
);

CREATE TABLE Review(
	name VARCHAR(20) NOT NULL, 
	time TIMESTAMP, 
	mid INT NOT NULL, 
	rating INT NOT NULL, 
	comment VARCHAR(500),
	FOREIGN KEY(mid) references Movie(id)
);

CREATE TABLE MaxPersonID(id INT NOT NULL);
CREATE TABLE MaxMovieID(id INT NOT NULL);












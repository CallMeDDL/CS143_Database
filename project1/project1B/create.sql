CREATE TABLE Movie(
	id INT NOT NULL, 
	title VARCHAR(100) NOT NULL, 
	year INT, 
	rating VARCHAR(10), 
	company VARCHAR(50),
	PRIMARY KEY(id)
		-- The primary key of Movie is id
) ENGINE = INNODB;

CREATE TABLE Actor(
	id INT NOT NULL, 
	last VARCHAR(20), 
	first VARCHAR(20), 
	sex VARCHAR(6), 
	dob DATE,
	dod DATE,
	PRIMARY KEY(id),
		-- The primary key of Actor is id
	CHECK ( DATEDIFF(dob, dod) < 0 AND sex IN ('Female', 'Male')) 
		-- Date of birth should be smaller than the date of death
		-- Sex should be either Female or Male
) ENGINE = INNODB;

CREATE TABLE Director(
	id INT NOT NULL, 
	last VARCHAR(20), 
	first VARCHAR(20), 
	dob DATE,
	dod DATE,
	PRIMARY KEY(id),
		-- The primary key of Director is id
	CHECK (DATEDIFF(dob, dod) < 0)
		-- Date of birth should be smaller than the date of death
) ENGINE = INNODB;

CREATE TABLE MovieGenre(
	mid INT NOT NULL, 
	genre VARCHAR(20), 
	FOREIGN KEY(mid) references Movie(id)
		-- mid is foreign key from Movie
) ENGINE = INNODB;

CREATE TABLE MovieDirector(
	mid INT NOT NULL, 
	did INT NOT NULL,
	FOREIGN KEY(mid) references Movie(id),
		-- mid is foreign key from Movie
	FOREIGN KEY(did) references Director(id)
		-- did is foreign key from Director
) ENGINE = INNODB;

CREATE TABLE MovieActor(
	mid INT NOT NULL, 
	aid INT NOT NULL,
	role VARCHAR(50) NOT NULL,
	FOREIGN KEY(mid) references Movie(id),
		-- mid is foreign key from Movie
	FOREIGN KEY(aid) references Actor(id)
		-- aid is foreign key from Actor
) ENGINE = INNODB;

CREATE TABLE Review(
	name VARCHAR(20) NOT NULL, 
	time TIMESTAMP, 
	mid INT NOT NULL, 
	rating INT NOT NULL, 
	comment VARCHAR(500),
	FOREIGN KEY(mid) references Movie(id)
		-- mid is foreign key from Movie
) ENGINE = INNODB;

CREATE TABLE MaxPersonID(id INT NOT NULL) ENGINE = INNODB;
CREATE TABLE MaxMovieID(id INT NOT NULL) ENGINE = INNODB;












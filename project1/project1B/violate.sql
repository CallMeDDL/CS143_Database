INSERT INTO Movie VALUES (4642, 'Harry Potter', 2000, NULL, NULL);
	-- A primary key id can not be duplicate, id 4642 has been used
INSERT INTO Actor VALUES (68143, 'Harry', 'Potter', 'Male', NULL, NULL);
	-- A primary key id can not be duplicate, id 68143 has been used
INSERT INTO Director VALUES (67530, 'Harry', 'Potter', NULL, NULL);
	-- A primary key id can not be duplicate, id 67530 has been used

INSERT INTO MovieGenre VALUES (67530, NULL);
	-- A foreign key mid must exist in reference table, Movie table doesn't have id 67530
INSERT INTO MovieDirector VALUES (67530, 2);
	-- A foreign key mid must exist in reference table, Movie table doesn't have id 67530
INSERT INTO MovieDirector VALUES (4734, 80000);
	-- A foreign key did must exist in reference table, Director table doesn't have id 80000
INSERT INTO MovieActor VALUES (67530, 69635, "King");
	-- A foreign key mid must exist in reference table, Movie table doesn't have id 67530
INSERT INTO MovieActor VALUES (4734, 80000, "King");
	-- A foreign key aid must exist in reference table, Actor table doesn't have id 80000
INSERT INTO Review VALUES ("comment", NULL, 67530, 1, NULL);
	-- A foreign key mid must exist in reference table, Movie table doesn't have id 67530

INSERT INTO Actor VALUES (68636, "Harry", "Potter", "Man", "1995-09-01", "2095-09-01");
	-- Sex should be either "Female" or "Male", not "Man"
INSERT INTO Actor VALUES (68636, "Harry", "Potter", "Man", "1995-09-01", "1994-09-01");
	-- Date of birth should be smaller than the date of death
INSERT INTO Director VALUES (68636, "Harry", "Potter", "1995-09-01", "1994-09-01");
	-- Date of birth should be smaller than the date of death
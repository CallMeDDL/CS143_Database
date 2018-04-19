-- Returns the first and last name string of actors in the movie "Die Another Day"

SELECT CONCAT(first, ' ', last) AS name
FROM Actor
INNER JOIN MovieActor ON
	MovieActor.aid = Actor.id 
INNER JOIN Movie ON
	MovieActor.mid = Movie.id AND Movie.title="Die Another Day";

-- Returns the number of actors who acted in multiple movies
SELECT COUNT(aid)
FROM (
	SELECT aid
	FROM MovieActor
	GROUP BY aid
	HAVING COUNT(mid) > 1
)multi_actor;

-- Return the number of directors who are actors at the same time
SELECT COUNT(did)
FROM (
	SELECT did
	FROM MovieDirector
	JOIN MovieActor ON 
		MovieActor.aid = MovieDirector.did
)actor_director;
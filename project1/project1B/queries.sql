
/*Returns the first and last name string of actors in the movie "Die Another Day"*/
SELECT CONCAT(Actor.first, ' ', Actor.last)
FROM  MovieActor, Actor, Movie
WHERE Movie.title="Die Another Day" AND Actor.id=MovieActor.aid AND MovieActor.mid=Movie.id;

/* Returns the number of actors who acted in multiple movies */
SELECT	COUNT(id)
FROM	(
		SELECT	Actor.id
		FROM	MoiveActor
		JOIN	Actor ON MovieActor.aid = Actor.id
		GROUP BY	id
		WHERE	COUNT(MovieActor.aid) > 1
) as A

/*Return the number of directors who was a actor before*/
SELECT	COUNT(did)
FROM	(
		SELECT	Actor.id
		FROM	Actor
		JOIN	Director ON Actor.id = Director.id
		JOIN	MovieActor ON Actor.id = MovieActor.aid
		JOIN	MovieDirector ON Director.id = MovieDirector.did
		GROUP BY	Actor.id
		WHERE	MoiveActor.mid = MovieDirector.mid 
) as B



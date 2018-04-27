<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
		<title>Show Movie Information</title>
		<meta name="viewport" content="width=device-width, initial-scale=1">

		<!-- link to Bootstrap -->
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
</head>
<body>
	<header class="blog-header py-3 bg-warning text-center">
		<a class="blog-header-logo text-white" href="home.php">
			<h1>Movie Databse Query Interface</h1>
		</a>
	</header>
	<div class="container-fluid">
		<div class="row">
			<nav class="col-md-3 d-none d-md-block bg-light sidebar">
				<br>
				<div class="sidebar-sticky">
					<ul class="nav flex-column">
						<h5>Input Option</h5>
						<li class="nav-item">
							<a class="nav-link  text-warning" href="add_people.php">Add an Actor or Director</a>
						</li>
						<li class="nav-item">
							<a class="nav-link text-warning" href="add_movie.php">Add Movie Information</a>
						</li>
						<li class="nav-item">
							<a class="nav-link text-warning" href="search_movie.php">Add Movie Comment</a>
						</li>
						<li class="nav-item">
							<a class="nav-link text-warning" href="search_movie.php">Add Movie and Actor Relation</a>
						</li>
						<li class="nav-item">
							<a class="nav-link text-warning" href="search_movie.php">Add Movie and Director Relation</a>
						</li>
					</ul>
				</div>
				<br><br>
				<div class="sidebar-sticky">
					<ul class="nav flex-column">
						<h5>Browsing Option</h5>
						<li class="nav-item">
							<a class="nav-link  text-warning" href="search_actor.php">Show Actor Information</a>
						</li>
						<li class="nav-item">
							<a class="nav-link  text-warning" href="search_movie.php">Show Movie Information</a>
						</li>
					</ul>
				</div>
			</nav>
			<div class="col-9">
				<br><br>
				<div class="container">
					<div class="row">
						<div class="col-1"></div>
						<div class="col-10">
							<h2>Show Movie Information</h2>
							<hr style="width: 100%; color: black; height: 1px;" />
						</div>
					</div>
				</div>
				<div class="container">
					<div class="row">
						<div class="col-2"></div>
						<div class="col-10">
							<h5>Movie Information:</h5>
						</div>
					</div>
				</div>
				<div class="container">
					<div class="row">
						<div class="col-2"></div>
						<div class="col-10">
							<?php
								$db = new mysqli('localhost', 'cs143', '', 'CS143');
								if($db->connect_errno > 0){
								die('Unable to connect to database [' . $db->connect_error . ']');
								}

								$id = 3563;//$_GET[""];
								//$title = $_GET[""];
								//$year = $_GET[""];
								$query1 = ("SELECT rating, company, year, title 
										   FROM Movie 
										   WHERE id = $id
										   ORDER BY rating, company, year, title;
										   ");

								$query2 = ("SELECT genre 
										    FROM MovieGenre 
										    WHERE mid = $id 
										    ORDER BY genre;
										   ");
								$rs1 = $db->query($query1);
								$rs2 = $db->query($query2);

								while($row = mysqli_fetch_row($rs1)) {
									$rating = $row[0];
									$company = $row[1];
									$year = $row[2];
									$title = $row[3];
								}
								while($row = mysqli_fetch_row($rs2)) {
									$genre = $row[0];
								}
								echo "Title: ".$title."( ".$year." )"."<br>";
								echo "Producer: ".$company."<br>";
								echo "MPAA Rating: ".$rating."<br>";
								echo "Genre: ".$genre."<br>";
							?>
						</div>
					</div>
				</div>
				<br><br>
				<div class="container">
					<div class="row">
						<div class="col-2"></div>
						<div class="col-10">
							<h5>Actors in the Movie:</h5>
						</div>
					</div>
				</div>
				<div class="container">
					<div class="row">
						<div class="col-2"></div>
						<div class="col-10">
							<?php
								$db = new mysqli('localhost', 'cs143', '', 'CS143');
								if($db->connect_errno > 0){
								die('Unable to connect to database [' . $db->connect_error . ']');
								}

								$id = 3563;//$_GET[""];
								//$title = $_GET[""];
								//$year = $_GET[""];
								$query3 = ("SELECT first, last, role
										   FROM Actor 
										   INNER JOIN MovieActor ON Actor.id = MovieActor.aid
										   WHERE MovieActor.mid = $id
										   ORDER BY last, first, role;
										   ");
								// $query4 = ("SELECT A.first, A.last, A.dob, A.dod
								// 		   FROM Director A 
								// 		   INNER JOIN MovieDirector B ON A.id = B.did
								// 		   WHERE B.mid = $id
								// 		   ORDER BY A.last, A.first, A.dob;
								// 		   ");
								$rs3 = $db->query($query3);
								// $rs4 = $db->query($query4);
								while($row = mysqli_fetch_row($rs3)) {
									$first1 = $row[0];
									$last1 = $row[1];
									$role  = $row[2];
									echo "Name: ".$first1." ".$last1."<br>";
									echo "Role: ".$role."<br>";
								}
								// while($row = mysqli_fetch_row($rs4)) {
								// 	$first2 = $row[0];
								// 	$last2 = $row[1];
								// 	$dob2 = $row[2];
								//	$dod2 = $row[3];
								//echo "Name: ".$first1." ".$last1."<br>";
								//echo "Role: ".$role."<br>";	
							?>
						</div>
					</div>
				</div>
				<br>
				<div class="container">
					<div class="row">
						<div class="col-2"></div>
						<div class="col-2">
							<form action="movie_actor.php" method="get">
								<input type="submit" class="btn btn-outline-warning btn-block" value="Add Actor"> 
							</form>
						</div>
						<div class="col-1"></div>
						<div class="col-2">
							<form action="movie_director.php" method="get">
								<input type="submit" class="btn btn-outline-warning btn-block" value="Add Director"> 
							</form>
						</div>
					</div>
				</div>
				<br><br>
				<div class="container">
					<div class="row">
						<div class="col-2"></div>
						<div class="col-10">
							<h5>Movie Comment:</h5>
						</div>
					</div>
				</div>
				<div class="container">
					<div class="row">
						<div class="col-2"></div>
						<div class="col-10">
							<?php
								$db = new mysqli('localhost', 'cs143', '', 'CS143');
								if($db->connect_errno > 0){
								die('Unable to connect to database [' . $db->connect_error . ']');
								}
								$id = 3563;//$_GET[""];
								$query4 = ("SELECT name, rating, comment 
											FROM Review 
											WHERE mid = $id;"
										  );
								$rs4 = $db->query($query4);

								while($row = mysqli_fetch_row($rs4)) {
									$name4 = $row[0];
									$rating4 = $row[1];
									$commnet4 = $row[2];
								}
								echo "Name: ".$name4."<br>";
								echo "Rating: ".$rating4."<br>";
								echo "Comment: ".$cpmment4."<br>";
							
							?>
						</div>
					</div>
				</div>
				<br>
				<div class="container">
					<div class="row">
						<div class="col-2"></div>
						<div class="col-2">
							<form action="comment.php" method="get">
								<input type="submit" class="btn btn-outline-warning btn-block" value="Add Comment">
							</form> 
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>

</body>
</html>

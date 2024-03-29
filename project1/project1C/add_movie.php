<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
    <title>Add New Movie</title>
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
				<br><br>
				<div class="sidebar-sticky">
					<ul class="nav flex-column">
						<h5>Searching Option</h5>
						<li class="nav-item">
							<a class="nav-link  text-warning" href="search.php">Search Actor or Movie</a>
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
							<h2>Add Movie Information</h2>
							<hr style="width: 100%; color: black; height: 1px;" />
						</div>
					</div>
				</div>
				<form action="add_movie.php" method="get">
					<div class="container">
						<div class="row">
							<div class="col-2"></div>
							<div class="col-2">Movie title</div>
							<div class="col-6">
								<input type="text" name="title" class="form-control">
							</div>
						</div>
					</div>
					<br>
					<div class="container">
						<div class="row">
							<div class="col-2"></div>
							<div class="col-2">Year:</div>
							<div class="col-6">
								<input type="number" name="year" class="form-control">
							</div>
						</div>
					</div>
					<br>
					<div class="container">
						<div class="row">
							<div class="col-2"></div>
							<div class="col-2">MPAA rating:</div>
							<div class="col-6">
								<select name="rating" class="form-control"> 
									<option value="PG-13">PG-13</option> 
									<option value="R" selected>R</option>
									<option value="PG">PG</option>
									<option value="NC-17">NC-17</option>
									<option value="surrendere">surrendere</option>
									<option value="G">G</option>
								</select>
							</div>
						</div>
					</div>
					<br>
					<div class="container">
						<div class="row">
							<div class="col-2"></div>
							<div class="col-2">Production company:</div>
							<div class="col-6">
								<input type="text" name="company" class="form-control">
							</div>
						</div>
					</div>
					<br>
					<div class="container">
						<div class="row">
							<div class="col-2"></div>
							<div class="col-2">Genre:</div>
							<div class="col-6">
								<input type="checkbox" name="genre[]" value="drama">
								<label for="Drama">Drama</label>
								<input type="checkbox" name="genre[]" value="comedy">
								<label for="Comedy">Comedy</label>
								<input type="checkbox" name="genre[]" value="romance">
								<label for="Romance">Romance</label>
								<input type="checkbox" name="genre[]" value="crime">
								<label for="Crime">Crime</label>
								<input type="checkbox" name="genre[]" value="horror">
								<label for="Horror">Horror</label>
								<input type="checkbox" name="genre[]" value="mystery">
								<label for="Mystery">Mystery</label>
								<input type="checkbox" name="genre[]" value="thriller">
								<label for="Thriller">Triller</label>
								<input type="checkbox" name="genre[]" value="action">
								<label for="Action">Action</label>
								<input type="checkbox" name="genre[]" value="adventure">
								<label for="Adventure">Adventure</label>
								<input type="checkbox" name="genre[]" value="fantasy">
								<label for="Fantasy">Fantasy</label>
								<input type="checkbox" name="genre[]" value="documentary">
								<label for="Documentary">Documentary</label>
								<input type="checkbox" name="genre[]" value="family">
								<label for="Family">Family</label>
								<input type="checkbox" name="genre[]" value="sci-fi">
								<label for="Sci-Fi">Sci-Fi</label>
								<input type="checkbox" name="genre[]" value="animation">
								<label for="Animation">Animation</label>
								<input type="checkbox" name="genre[]" value="musical">
								<label for="Musical">Musical</label>
								<input type="checkbox" name="genre[]" value="war">
								<label for="War">War</label>
								<input type="checkbox" name="genre[]" value="western">
								<label for="Western">Western</label>
								<input type="checkbox" name="genre[]" value="adult">
								<label for="Adult">Adult</label>
								<input type="checkbox" name="genre[]" value="short">
								<label for="Short">Short</label>
							</div>
						</div>
					</div>
					<br><br>
					<div class="container">
						<div class="row">
							<div class="col-5"></div>
							<div class="col-2">
								<input type="submit" class="btn btn-outline-warning btn-block" value="Submit"> 
							</div>
						</div>
					</div>
				</form>
				<div class="container">
					<div class="row">
						<div class="col-1"></div>
						<div class="col-10">
							<br>
							<h2>Result</h2>
							<hr style="width: 100%; color: black; height: 1px;" />
							<center>
								<?php
								
								$db = new mysqli('localhost', 'cs143', '', 'CS143');
								if($db->connect_errno > 0){
								die('Unable to connect to database [' . $db->connect_error . ']');
								}
							 	$title = $_GET["title"];
							 	$year = $_GET["year"];
							 	$rating = $_GET["rating"];
							 	$company = $_GET["company"];
							 	$movieGenre = $_GET["genre"];
							 	
							 	
							 	// Issuing Queries
							 	if (isset($_GET["title"]) && isset($_GET["year"]) && isset($_GET["rating"])){
								 	$db->query("UPDATE MaxMovieID SET id = id + 1;");
								 	$rs = $db->query("SELECT id FROM MaxMovieID;");
								 	$row = mysqli_fetch_row($rs);
								 	$id = $row[0];
								 	$query = ("INSERT INTO Movie VALUES($id, '$title', $year, '$rating', '$company');");
								 	if (!($rs1 = $db->query($query))){
										$errmsg = $db->error;
										print "<h5>Query failed: $errmsg</h5> <br />";
										exit(1);
									}
									else {
										print '<h5>Succesfully Add New Movie into our database!</h5><br>';
										echo "Title: ".$title."<br>";
										echo "Year: ".$year."<br>";
										echo "Rating: ".$rating."<br>";
										echo "Company: ".$company."<br>";
										echo "Genre: ";
									}
								 	$genreNum = 0;
								 	if (empty($movieGenre)) {
								 		echo "No Movie Genre set !";
								 	}
								 	else {
										foreach ($movieGenre as $Genre){
											$db->query("INSERT INTO MovieGenre VALUES($id, '$Genre');");
											echo $Genre. " ";
										}
									}
								}	
								
								?>
							</center>
							<br><br><br><br><br><br><br>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>

</body>
</html>

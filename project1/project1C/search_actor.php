<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
		<title>Search a Actor</title>
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
							<h2>Search a Actor</h2>
							<hr style="width: 100%; color: black; height: 1px;" />
						</div>
					</div>
				</div>
				<form action="search_actor.php" method="get">
					<div class="container">
						<div class="row">
							<div class="col-2"></div>
							<div class="col-2">Actor name:</div>
							<div class="col-6">
								<input type="text" name="name" class="form-control">
							</div>
						</div>
					</div>
					<br><br>
					<div class="container">
						<div class="row">
							<div class="col-5"></div>
							<div class="col-2">
								<input type="submit" class="btn btn-outline-warning btn-block" value="Search"> 
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
								<a class="nav-link  text-warning" href="actor_info.php">Handsome Tianyi</a>
								<?php
								
								$db = new mysqli('localhost', 'cs143', '', 'CS143');
								if($db->connect_errno > 0){
								die('Unable to connect to database [' . $db->connect_error . ']');
								}
								$name = $_GET["name"];
								if ($name != "") {
									$query = ("SELECT id, dob, first, last, dod
										   FROM Actor 
										   WHERE concat(first, ' ', last) REGEXP '$name'
										   ORDER BY last, first, dob, id;
									          ");
								}
								else {
									$query = ("SELECT id, dob, first, last, dod
									           FROM Actor 
									           ORDER BY last, first, dob, id;
									          ");
								
								}
								$rs = $db->query($query);

								while($row = mysqli_fetch_row($rs)) {
									$id = $row[0];
									$dob = $row[1];
									$first = $row[2];
									$last = $row[3];
									$dod = $row[4];
									echo "Actor Name: ".$first." ";
									echo $last."<br>";
									echo "Actor Data of Birth: ".$dob."<br>";
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

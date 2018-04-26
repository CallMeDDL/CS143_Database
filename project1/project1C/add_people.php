<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
		<title>Add Actor or Director</title>
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
							<h2>Add An Actor or Director</h2>
							<hr style="width: 100%; color: black; height: 1px;" />
						</div>
					</div>
				</div>
				<form action="add_people.php" method="get">
					<div class="container">
						<div class="row">
							<div class="col-2"></div>
							<div class="col-2">Type:</div>
							<div class="col-6">
								<input type="radio" name="type" value="actor">
								<label for="contactChoice1">Actor</label>
								<input type="radio" name="type" value="director">
								<label for="contactChoice1">Director</label>
							</div>
						</div>
					</div>
					<br>
					<div class="container">
						<div class="row">
							<div class="col-2"></div>
							<div class="col-2">First name:</div>
							<div class="col-6">
								<input type="text" name="fname" class="form-control">
							</div>
						</div>
					</div>
					<br>
					<div class="container">
						<div class="row">
							<div class="col-2"></div>
							<div class="col-2">Last name:</div>
							<div class="col-6">
								<input type="text" name="lname" class="form-control">
							</div>
						</div>
					</div>
					<br>
					<div class="container">
						<div class="row">
							<div class="col-2"></div>
							<div class="col-2">Sex:</div>
							<div class="col-6">
								<input type="radio" name="sex" value="male">
								<label for="contactChoice1">Male</label>
								<input type="radio" name="sex" value="female">
								<label for="contactChoice1">Female</label>
							</div>
						</div>
					</div>
					<br>
					<div class="container">
						<div class="row">
							<div class="col-2"></div>
							<div class="col-2">Date of birth:</div>
							<div class="col-6">
								<input type="text" name="birth" class="form-control">
							</div>
						</div>
					</div>
					<br>
					<div class="container">
						<div class="row">
							<div class="col-2"></div>
							<div class="col-2">Date of death:</div>
							<div class="col-6">
								<input type="text" name="death" class="form-control">
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
								// Establishing a Connection
								$db = new mysqli('localhost', 'cs143', '', 'CS143');
								if($db->connect_errno > 0){
								die('Unable to connect to database [' . $db->connect_error . ']');
								}
							 	$type = $_GET["type"];
							 	$fname = $_GET["fname"];
							 	$lname = $_GET["lname"];
							 	$sex = $_GET["sex"];
							 	$birth = $_GET["birth"];
							 	$death = $_GET["death"];
							 	// Issuing Queries
							 	$db->query("UPDATE MaxPersonID SET id = id + 1;");
							 	$rs = $db->query("SELECT id FROM MaxPersonID;");
							 	$row = mysqli_fetch_row($rs);
							 	$id = $row[0];
							 	if ($type == "actor") {
							 		if ($death != "") {
							 			$query = "INSERT INTO Actor VALUES($id, '$lname', '$fname', '$sex', '$birth', '$death');";
							 		}
							 		else {
							 			$query = "INSERT INTO Actor VALUES($id, '$lname', '$fname', '$sex', '$birth', NULL);";
							 		}
							 	}
								else {
							 		if ($death != "") {
							 			$query = "INSERT INTO Actor VALUES($id, '$lname', '$fname', '$birth', '$death');";
							 		} 
							 		else {
										$query = "INSERT INTO Actor VALUES($id, '$lname', '$fname', '$birth', NULL);";
									}
							 	}
							 	$db->query($query);
								$db->close();
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

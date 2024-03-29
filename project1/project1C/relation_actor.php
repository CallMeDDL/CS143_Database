<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
		<title>Add Actor and Movie Relation</title>
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
							<h2>Add Actor and Movie Relation</h2>
							<hr style="width: 100%; color: black; height: 1px;" />
						</div>
					</div>
				</div>
				<form action="relation_actor.php" method="get">
					<div class="container">
						<div class="row">
							<div class="col-2"></div>
							<div class="col-2">Movie name:</div>
							<div class="col-6">
								<?php
								$mid = $_GET["mid"];
								$db = new mysqli('localhost', 'cs143', '', 'CS143');
								if($db->connect_errno > 0){
								die('Unable to connect to database [' . $db->connect_error . ']');
								}
								$query1 = ("SELECT title
										    FROM Movie
										    WHERE Movie.id = $mid
										   ");
								$rs1 = $db->query($query1);
								while($row = mysqli_fetch_row($rs1)) {
									$title = $row[0];
								}
								echo $title;	
								?> 
							</div>
						</div>
					</div>
					<br>
					<div class="container">
						<div class="row">
							<div class="col-2"></div>
							<div class="col-2">Actor name:</div>
							<div class="col-6">
								<?php
								$aid = $_GET["aid"];
								$db = new mysqli('localhost', 'cs143', '', 'CS143');
								if($db->connect_errno > 0){
								die('Unable to connect to database [' . $db->connect_error . ']');
								}
								$query1 = ("SELECT first, last
										    FROM Actor 
										    WHERE Actor.id = $aid
										   ");
								$rs1 = $db->query($query1);
								while($row = mysqli_fetch_row($rs1)) {
									$first = $row[0];
									$last = $row[1];
								}
								echo $first. " " .$last;	
								?> 
							</div>
						</div>
					</div>
					<br>
					<div class="container">
						<div class="row">
							<div class="col-2"></div>
							<div class="col-2">Role:</div>
							<div class="col-6">
								<input type="text" name="role" class="form-control">
							</div>
						</div>
					</div>
					<br><br>
					<div class="container">
						<div class="row">
							<div class="col-5"></div>
							<div class="col-2">
								<input type="submit" class="btn btn-outline-warning btn-block" value="Add">
								<?php
								$mid = $_GET["mid"];
								$aid = $_GET["aid"];
								print '<input type="hidden" name="mid" value="' .$mid. '">';
								print '<input type="hidden" name="aid" value="' .$aid. '">';
								?> 
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
								$mid = $_GET["mid"];
								$aid = $_GET["aid"];
								$role = $_GET["role"];
								if (isset($_GET["role"])){
									if ($mid != null && $aid != null) {
										$query = ("INSERT INTO MovieActor VALUES($mid, $aid, '$role');");
										if (!($rs = $db->query($query))){
												$errmsg = $db->error;
												print "<h5>Query failed: $errmsg</h5> <br />";
												exit(1);
										}
										else {
										 	print '<h5>Succesfully Add Movie and Director Relation into our database!</h5><br>';
											echo "Movie ID: ".$mid."<br>";
											echo "Actor ID: ".$aid."<br>";
											echo "Actor Role: ".$role."<br>";
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

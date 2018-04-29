<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
		<title>Show Actor Information</title>
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
				<br><br><br><br><br><br><br><br><br><br>
			</nav>
			<div class="col-9">
				<br><br>
				<div class="container">
					<div class="row">
						<div class="col-1"></div>
						<div class="col-10">
							<h2>Show Actor Information</h2>
							<hr style="width: 100%; color: black; height: 1px;" />
						</div>
					</div>
				</div>
				<div class="container">
					<div class="row">
						<div class="col-2"></div>
						<div class="col-10">
							<h5>Actor Information:</h5>
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

								$id = $_GET["id"];
								//$title = $_GET[""];
								//$year = $_GET[""];
								$query1 = ("SELECT first, last, sex, dob, dod
										    FROM Actor 
										    WHERE Actor.id = $id
										    ORDER BY first, last, sex, dob, dod;
										   ");
								$rs1 = $db->query($query1);
								while($row = mysqli_fetch_row($rs1)) {
									$first1 = $row[0];
									$last1 = $row[1];
									$sex1 = $row[2];
									$dob1 = $row[3];
									$dod1 = $row[4];
								}
								echo "Name: ".$first1." ".$last1."<br>";
								echo "Sex: ".$sex1."<br>";
								echo "Date of Birth: ".$dob1."<br>";
								if ($dod1 != null) {
									echo "Date of Birth: ".$dod1."<br>";
								}
								else {
									echo "Date of Death: "."Still Alive"."<br>";
								}
							?>
						</div>
					</div>
				</div>
				<br><br>
				<div class="container">
					<div class="row">
						<div class="col-2"></div>
						<div class="col-10">
							<h5>Actor's Movie Role:</h5>
						</div>
					</div>
				</div>
				<div class="container">
					<div class="row">
						<div class="col-2"></div>
						<div class="col-8">
							<?php
							
								// still has a bug
								$db = new mysqli('localhost', 'cs143', '', 'CS143');
								if($db->connect_errno > 0){
								die('Unable to connect to database [' . $db->connect_error . ']');
								}
								
								$id = $_GET["id"];
								//$year = $_GET[""];
								$query2 = ("SELECT id, title, role 
										    FROM Movie 
										    INNER JOIN MovieActor ON Movie.id = MovieActor.mid
										    WHERE MovieActor.aid = $id
										    ORDER BY role, title;
										   ");
								if (!($rs2 = $db->query($query2))) {
									$errmsg = $db->error;
									print "<h5>Query failed: $errmsg</h5> <br />";
									exit(1);
								}
								else {
									print '<table class="table table-bordered">
									<thead class="thead-light">
									<tr>
									<th scope="col">Movie Name</th>
									<th scope="col">Role</th>
									</tr>
									</thead>
									<tbody>';
									while($row = mysqli_fetch_row($rs2)) {
										$id = $row[0];
										$title = $row[1];
										$role = $row[2];
										print '<tr><th scope="row"><a class="nav-link  text-warning" href="movie_info.php?id=' .$id. '">' .$title . '</a></th>';
										print '<td>' . $role . '</td></tr>';
									}
									print '</tbody>
									</table>';
								}
							?>
						</div>
					</div>
				</div>
				<br>
			</div>
		</div>
	</div>

</body>
</html>

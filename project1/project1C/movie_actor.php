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
				<form action="movie_actor.php" method="get">
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
								<?php
								$mid = $_GET["mid"];
								print '<input type="hidden" name="mid" value="' .$mid. '">';
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
								$name = $_GET["name"];
								if (isset($_GET["name"])){
									if ($name != "") {
										$query = ("SELECT id, dob, first, last, dob
											   FROM Actor 
											   WHERE concat(first, ' ', last) REGEXP '$name'
											   ORDER BY last, first, dob, id;
											  ");
									}
									else {
										$query = ("SELECT id, dob, first, last, dob
											   FROM Actor 
											   ORDER BY last, first, dob, id;
											  ");
									}
								
									$rs = $db->query($query);
									print '<table class="table table-bordered">
										<thead class="thead-light">
										<tr>
										<th scope="col">Actor Name</th>
										<th scope="col">Birth</th>
										</tr>
										</thead>
										<tbody>';
									$mid = $_GET["mid"];
									while($row = mysqli_fetch_row($rs)) {
										$id = $row[0];
										$dob = $row[1];
										$first = $row[2];
										$last = $row[3];
										$dod = $row[4];
										print '<tr><th scope="row"><a class="nav-link  text-warning" href="relation_actor.php?aid=' .$id. '&mid=' .$mid. '">' .$first. ' ' .$last. '</a></th>';
										print '<td>' . $dod . '</td></tr>';
									}
									print '</tbody>
										</table>';
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
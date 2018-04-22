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
		<a class="blog-header-logo text-white">
			<h1>Movie Databse Query Interface</h1>
		</a>
	</header>
	<br>
	<div class="container">
		<div class="row">
			<div class="col-1"></div>
			<div class="col-10">
				<h2>Add An Actor or Director</h2>
				<hr style="width: 100%; color: black; height: 1px;" />
			</div>
		</div>
	</div>
	<form action="query.php" method="get">
		<div class="container">
			<div class="row">
				<div class="col-2"></div>
				<div class="col-2">Type:</div>
				<div class="col-4">
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
				<div class="col-4">
					<input type="text" name="fname">
				</div>
			</div>
		</div>
		<br>
		<div class="container">
			<div class="row">
				<div class="col-2"></div>
				<div class="col-2">Last name:</div>
				<div class="col-4">
					<input type="text" name="lname">
				</div>
			</div>
		</div>
		<br>
		<div class="container">
			<div class="row">
				<div class="col-2"></div>
				<div class="col-2">Sex:</div>
				<div class="col-4">
					<input type="radio" name="sex" value="male">
					<label for="contactChoice1">Male</label>
					<input type="radio" name="type" value="female">
					<label for="contactChoice1">Female</label>
				</div>
			</div>
		</div>
		<br>
		<div class="container">
			<div class="row">
				<div class="col-2"></div>
				<div class="col-2">Date of birth:</div>
				<div class="col-4">
					<input type="text" name="birth">
				</div>
			</div>
		</div>
		<br>
		<div class="container">
			<div class="row">
				<div class="col-2"></div>
				<div class="col-2">Date of death:</div>
				<div class="col-4">
					<input type="text" name="death">
				</div>
			</div>
		</div>
		<br><br>
		<div class="container">
			<div class="row">
				<div class="col-3"></div>
				<div class="col-4">
					<input type="submit" class="btn btn-outline-warning" value="Submit"> 
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

					// Issuing Queries
					$query = $_GET["query"];
					if (!is_null($query)){
						if (!($rs = $db->query($query))){
							$errmsg = $db->error;
							print "Query failed: $errmsg <br />";
							exit(1);
						}

						// Retrieving Results
						if ($rs->field_count > 0) {
							$field = array();
							print '<table class="table table-bordered" ><thead class="thead-light"><tr>';
							while ($finfo = $rs->fetch_field()) {
								$field[] = $finfo->name;
								print '<th scope="col">' . $finfo->name . '</th>';
							}
							print '</tr></thead><tbody>';
							while($row = $rs->fetch_assoc()) {
								print '<tr>';
								for ($i = 0; $i < $rs->field_count; $i++) {
									print '<td>' . $row[$field[$i]] . '</td>';
								}
								print '</tr>';
							}
							print '</tbody></table>';
						}else {
							print "No result";
						}

						// Free Result and Close Database
						$rs->free();
					}
					$db->close();
					?>
				</center>
			</div>
		</div>
	</div>

</body>
</html>
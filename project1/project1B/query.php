<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
    <title>Query</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- link to Bootstrap -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
</head>
<body>
	<header class="blog-header py-3 bg-warning text-center">
		<a class="blog-header-logo text-white">
			<h1>Databse Query Interface</h1>
		</a>
	</header>
	<br>
	<div class="container">
		<div class="row">
			<div class="col-1"></div>
			<div class="col-10">
				<h2>Input</h2>
				<hr style="width: 100%; color: black; height: 1px;" />
			</div>
		</div>
	</div>
	<form action="query.php" method="get">
		<div class="container">
			<div class="row">
				<div class="col-2"></div>
				<div class="col-2">
					<h5>Query:</h5>
					<br>
					<input type="submit" class="btn btn-outline-warning" value="Submit"> 
				</div>
				<div class="col-4">
					<textarea name="query" rows="5" style="width: 100%;""></textarea>
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
					$db = new mysqli('localhost', 'cs143', '', 'TEST');
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
						while($row = $rs->fetch_assoc()) {
							$sid = $row['sid'];
							$name = $row['name'];
							$email = $row['email'];
							print "$sid, $name, $email<br />";
						}
						print 'Total results: ' . $rs->num_rows;

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
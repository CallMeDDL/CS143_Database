<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
    <title>Add Movie Actor Relation</title>
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
				<h2>Add Movie and Actor Relation</h2>
				<hr style="width: 100%; color: black; height: 1px;" />
			</div>
		</div>
	</div>
	<form action="movie_actor.php" method="get">
		<div class="container">
			<div class="row">
				<div class="col-2"></div>
				<div class="col-2">Movie title</div>
				<div class="col-4">
					<select name="title" class="form-control"> 
						<option value="PG-13">PG-13</option> 
						<option value="R" selected>R</option>
					</select>
				</div>
			</div>
		</div>
		<br>
		<div class="container">
			<div class="row">
				<div class="col-2"></div>
				<div class="col-2">Actor:</div>
				<div class="col-4">
					<select name="actor" class="form-control"> 
						<option value="PG-13">PG-13</option> 
						<option value="R" selected>R</option>
					</select>
				</div>
			</div>
		</div>
		<br>
		<div class="container">
			<div class="row">
				<div class="col-2"></div>
				<div class="col-2">Role:</div>
				<div class="col-4">
					<input type="text" name="role" class="form-control">
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

					?>
				</center>
			</div>
		</div>
	</div>

</body>
</html>
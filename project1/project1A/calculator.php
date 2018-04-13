<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
    <title>Calculator</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- link to Bootstrap -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
</head>
<body>
	<header class="blog-header py-3 bg-warning text-center">
        <a class="blog-header-logo text-white">
            <h1>Calculator</h1>
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
	<form action="calculator.php" method="get">
		<div class="container">
			<div class="row">
				<div class="col-2"></div>
				<div class="col-2">
					<h5>Expression:</h5>
				</div>
				<div class="col-3">
					<input type="text" name="exp">
				</div>
				<div class="col-2">
					<input type="submit" class="btn btn-outline-warning" value="Run" >		
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
					$reg = $_GET["exp"];
					$regex = "/[^\d-+\*\/\.]/";
					preg_match($regex, $reg, $matches, PREG_OFFSET_CAPTURE);
					//print_r($matches);
					if (count($matches) == 0) {
						eval("\$res = $reg;");
						echo $reg . "=" . $res;

					} else {
						echo "Invalid Expression";

					}
					?>
				</center>
			</div>
		</div>
	</div>

</body>
</html>
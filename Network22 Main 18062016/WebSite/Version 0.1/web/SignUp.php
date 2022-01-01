<!DOCTYPE HTML>
<!--
	Spatial by TEMPLATED
	templated.co @templatedco
	Released for free under the Creative Commons Attribution 3.0 license (templated.co/license)
-->
<html>
	<head>
		<title>Networks United</title>
		<meta http-equiv="content-type" content="text/html; charset=utf-8" />
		<meta name="description" content="" />
		<meta name="keywords" content="" />
		<!--[if lte IE 8]><script src="js/html5shiv.js"></script><![endif]-->
		<script src="js/jquery.min.js"></script>
		<script src="js/skel.min.js"></script>
		<script src="js/skel-layers.min.js"></script>
		<script src="js/init.js"></script>
		<link rel="stylesheet" href="css/skel.css" />
		<link rel="stylesheet" href="css/style2.css" />
		<link rel="stylesheet" href="css/style-xlarge.css" />
		<link rel="stylesheet" type="text/css" href="form.css"/>
	</head>
	<body class="landing" id="back">

		<!-- Header -->
			<header id="header" class="alt">
				
				<h1 id="navb"><strong ><a  href="index.html"><img src="logo.png">NetworksUnited</a></strong></h1></img>
				<nav id="nav">
					<ul>
						<li><a href="index.html">Home</a></li>
						<li><a href="generic.html">What Is It</a></li>
						<li><a href="elements.html">How It Works</a></li>
						<li><a href="elements.html">DownLoad The App</a></li>
					</ul>
				</nav>
			</header>

		<!-- Main -->
			<section id="main" class="wrapper">
				<div class="container">

					<header class="major special">
						<h2>Ready to SignUp?</h2>
						<p> <br> </p>
						
					</header>
					<?php
						//error_reporting(0);
						function Redirect($url, $permanent = false)
						{
							header('Location: ' . $url, true, $permanent ? 301 : 302);

							exit();
						}
						if($_POST['submit']==TRUE){
							$server="localhost";
							$user="tester";
							$pass="123123123";
							
							if(strlen($_POST['password'])<5){
								
								echo '<font color="red">Password is too weak :/</font>';
								die();
							}
							
							
							
							$conn = new mysqli($server,$user,$pass);
							$conn->query("use users;");
							if($conn->query("insert into ".$_POST['country']."  values('".$_POST['name']."','".$_POST['surname']."',0,'".$_POST['email']."','".$_POST['password']."');")){
								Redirect('http://www.google.com', false);
							}
						}
	
					?>
					<section class="body">
					
					<form method="post" action="SignUp.php">
						<label>Name</label>
						<input  name="name" placeholder="Name">
		
						<label>Surname</label>
						<input  name="surname"  placeholder="Surname">
						
						<label>Email</label>
						<input name="email" type="email" placeholder="Email">
						
						<label>Password</label>
						<input name="password" type="password" placeholder="Password">
						<?php if($_POST['submit'] and strlen($_POST['password'])>25){ ?>
							<font color="red">password is too big to be true bro! <br></font>
						
						<?php } ?>
						<select name="country" id="selection-country">
							<option value="greece">greece</option>
							<option value="usa">Usa</option>
							<option value="None">TestCountry</option>
							<option value="None">TestCountry</option>
							<option value="None">TestCountry</option>
							<option value="None">TestCountry</option>
							<option value="None">TestCountry</option>
							<option value="None">TestCountry</option>
							
						</select>
						<input name="submit" type="submit" value="Download the App">
						
						
					</form>
	
					</section>
		<!-- Footer -->
	<footer id="footer">
				<div class="container">
					<ul class="icons">
						<li><a href="#" class="icon fa-facebook"></a></li>
						<li><a href="#" class="icon fa-twitter"></a></li>
						<li><a href="#" class="icon fa-instagram"></a></li>
					</ul>
					<ul class="copyright">
						<li>© 2016-2017 NetworksUnited All Rights Reserved</li>
						<li>Design: <a href="https://www.facebook.com/Atticadreamer">by StefStef</a></li>
						<!--<li>Images: <a href="http://unsplash.com">Unsplash</a></li>-->
					</ul>
				</div>
			</footer>

	</body>
</html>
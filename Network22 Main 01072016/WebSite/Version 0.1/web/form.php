<?php
	$name = isset($_POST['name']);
	$surname = isset($_POST['name']);
	$email = isset($_POST['email']);
	$password = isset($_POST['password']);

	if(isset($_POST['submit'])){
		$server="localhost";
		$port=8888;
		$user="tester";
		$pass="102030102030102030";
		$db_name="GREECE";
		$db_table="NEW USERS";
							
		$conn = new mysqli($server,$user,$pass);
							
							
	}
	
?>
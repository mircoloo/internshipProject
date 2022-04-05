<?php   
include 'config.php';
$username = "root";
$password = "";
$server = "localhost";
$db = "smishingDB";

$conn = mysqli_connect($server, $username, $password, $db);

if($conn){
    ?>
        <script>
        /*alert('Connection Successfull');
        </script>
    <?php
}else{
 die("No connection" . mysqli_connect_error());
}  
?>
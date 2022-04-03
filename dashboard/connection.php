<?php   
$username = "mirco";
$password = "123";
$server = "192.168.1.108";
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
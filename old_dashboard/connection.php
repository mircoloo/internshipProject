<?php   
include 'config.php';
$username = $GLOBALS['USERNAME'];
$password = $GLOBALS['PASSWORD'];
$server = $GLOBALS['SERVER'];
$db = $GLOBALS['DB'];

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
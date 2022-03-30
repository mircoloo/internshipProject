<?php
    if (!function_exists('mysqli_init') && !extension_loaded('mysqli')) {
        echo 'We don\'t have mysqli!!!';
    } else {
        echo 'Phew we have it!';
    }
    $mysqli = new MySQLi('localhost', 'mirco', '123', 'smishingDB');
    $query1 = mysqli_query($mysqli, "select * from num")

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
</body>
</html>
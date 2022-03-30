<?php

    include 'connection.php';
    $select_query = "SELECT * FROM num";
    $query = mysqli_query($conn, $select_query);
    $num =  mysqli_num_rows($query);
    echo $num;


?>
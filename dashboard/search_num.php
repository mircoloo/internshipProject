<?php
    require 'connection.php';
    if($_SERVER['REQUEST_METHOD'] == 'POST'){
        $to_search = $_REQUEST['number'];
        $query = "SELECT *  FROM teldata WHERE number = " . $to_search;
        $result = mysqli_query($conn, $query);
        if (mysqli_num_rows($result)>0){
            while($row = mysqli_fetch_assoc($result)){
                #echo print_r($row);      
                foreach($row as &$el){
                    echo $el . "<br>";
                }
            }
        }else{
            echo "Numero non trovato";
        }
            

    }



?>
<?php

    include_once 'classes/dataClass.php';


    if(isset($_GET['request'])){
        print_r($_GET['request']);
        switch($_GET['request']){
            case "all": 
                $response = DataClass::getData();
                print_r($response); 
                break;
        }
    }

?>
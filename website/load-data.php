<?php

ini_set('display_errors', '1');
include "DBconnection.php";


function getData($conn, $query)
{
    $result = mysqli_query($conn, $query);
    while ($rows = mysqli_fetch_assoc($result)) {
?>
        <tr>
            <td data-label="Number"><?php echo $rows['number']; ?></td>
            <td data-label="Comment"><?php echo $rows['comment']; ?></td>
            <td data-label="Type"><?php echo $rows['type']; ?></td>
            <td data-label="Researchs"><?php if ($rows['researchs'] != -1) {
                                            echo $rows['researchs'];
                                        } else {
                                            echo "--";
                                        }; ?></td>
            <td data-label="Score"><?php echo $rows['score']; ?></td>
            <td data-label="Source"><?php echo $rows['source']; ?></td>
            <td data-label="Source"><?php echo $rows['organization']; ?></td>
        </tr>
<?php
    }
}



if ($_SERVER['REQUEST_METHOD'] == "GET") {
    echo  "<h1>Page is not reachable using GET methods</h1>";
    print_r($_GET);
} else {
    //check the post requests
    if (isset($_POST['commentCount'])) {
        $commentNewCount = $_POST['commentCount'];
        $GLOBALS['COMMENT_COUNT'] = $commentNewCount;
        $query = "select * from teldata limit " . $GLOBALS['COMMENT_COUNT'];
        getData($conn, $query);
    }


    if (isset($_POST['query'])) {
        switch ($_POST['query']) {
            case "Sicuro":
                $query = "SELECT * FROM teldata WHERE Type = '" . $_POST['query'] . "'";
                getData($conn, $query);
                break;

            case "all":
                $query = "SELECT * FROM teldata";
                getData($conn, $query);
                break;

            case "truffa":
                $query = "SELECT * FROM teldata  WHERE Type = 'Truffa / Chiamata Preregistrata' OR Type = 'Truffa'";
                getData($conn, $query);
                break;
            case "telemarketing":
                $query = "SELECT * FROM teldata  WHERE Type='Telemarketing'";
                getData($conn, $query);
                break;
            case "numero serio":
                $query = "SELECT * FROM teldata  WHERE Type='Sicuro' OR Type='Numero serio'";
                getData($conn, $query);
                break;
            case "sconosciuto":
                $query = "SELECT * FROM teldata  WHERE Type='Sconosciuto (1)'";
                getData($conn, $query);
                break;

        }
    }
}

if(isset($_POST['score'])){
        $query = "SELECT * FROM teldata WHERE Score = -1 OR Score >= " . $_POST['score'];    
        getData($conn, $query);   
}
?>
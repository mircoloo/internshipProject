<?php
ini_set('display_errors', '1');
require 'connection.php';
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Smishing dashboard</title>
    <!-- MATERIAL ICONS -->
    <link href="https://fonts.googleapis.com/css?family=Material+Icons|Material+Icons+Outlined|Material+Icons+Two+Tone|Material+Icons+Round|Material+Icons+Sharp" rel="stylesheet">
    <link rel="stylesheet" href="style.css">
</head>

<body>
    <div class="containter">
        <div class="left">

            <ul>
                <li>
                    <a href="#">
                        <span class="icon"><span class="material-icons-round">security_update_warning</span></span>
                        <span class="title">Smis<span style="color: #d43;">hing</span></span>
                    </a>

                </li>
                <li>
                    <a href="#">
                        <span class="icon"><span class="material-icons-round">grid_view</span></span>
                        <span class="title">Dashboard</span>
                    </a>
                </li>
                <li>
                    <a href="#">
                        <span class="icon"><span class="material-icons-round">query_stats</span></span>
                        <span class="title">Statistic</span>
                    </a>
                </li>
                <li>
                    <a href="#">
                        <span class="icon"><span class="material-icons-round">help</span></span>
                        <span class="title">Help</span>
                    </a>
                </li>
            </ul>
        </div>
        <div class="main">
            <div class="topbar">
                <div class="toggle">
                    <span class="material-icons-round">menu</span>
                </div>
            </div>
        </div>
        <div class="right">

        </div>
    </div>
</body>

</html>
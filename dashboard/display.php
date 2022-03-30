<?php
    $conn = mysqli_connect('localhost', 'mirco', '123', 'smishingDB');

    $sql = "SELECT * FROM 'numeri'";

    $result = msqli_query($conn, );
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

        <!-- STYLESHEET -->
        <link rel="stylesheet" href="./style.css">
    </head>

    <body>
        <div class="container">
            <aside>
                <div class="top">
                    <div class="logo">
                        <img src="./icons/logo.png" alt="">
                        <h2>SMIS<span class="danger">HING</span></h2>
                    </div>
                </div>
                <div class="close" id="close-btn">
                    <span class="material-icons-round">close</span>
                </div>

                <div class="sidebar">
                    <a href="#">
                        <span class="material-icons-round">grid_view</span>
                        <h3>Dashboard</h3>
                    </a>

                    <a href="#">
                        <span class="material-icons-round">query_stats</span>
                        <h3>Analytics</h3>
                    </a>

                    <a href="#">
                        <span class="material-icons-round">logout</span>
                        <h3>Logout</h3>
                    </a>

                </div>

            </aside>
            <!-------------------------------------- END OF ASIDE ------------------------------------->
            <main>
                <div class="recent-comments">
                    <h1>Recents comments</h1>
                    <table>
                        <thead>
                            <tr>
                                <th>Number</th>
                                <th>Comment</th>
                                <th>Type</th>
                                <th>Score</th>
                            </tr>
                            
                        </thead>
                        <tbody>
                            <tr>
                                <td>3458382843</td>
                                <td>Numero pericoloso</td>
                                <td>Truffa</td>
                                <td class="danger">2</td>
                            </tr>
                            <tr>
                                <td>3458382843</td>
                                <td>Numero pericoloso</td>
                                <td>Truffa</td>
                                <td class="danger">2</td>
                            </tr>
                            <tr>
                                <td>3458382843</td>
                                <td>Numero pericoloso</td>
                                <td>Truffa</td>
                                <td class="danger">2</td>
                            </tr>
                            <tr>
                                <td>3458382843</td>
                                <td>Numero pericoloso</td>
                                <td>Truffa</td>
                                <td class="danger">2</td>
                            </tr>
                            <tr>
                                <td>3458382843</td>
                                <td>Numero pericoloso</td>
                                <td>Truffa</td>
                                <td class="danger">2</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                
            </main>
            <!----------------------------END OF MAIN-------------------------------->
            <div class="right">
                <div class="top">
                    <button id="menu-btn">
                        <span class="material-icons-round">menu</span>
                    </button>
                    <div class="theme-toggler">
                        <span class="material-icons-round active">light_mode</span>
                        <span class="material-icons-round">dark_mode</span>
                    </div>
                </div>
            </div>
            <!-- END OF TOP -->
            <div class="recents-updates">
                <h2>Recents Updates</h2>
                <div class="updates">
                    <div class="update">
                        
                    </div>
                </div>
            </div>
        </div>

        

    </body>

</html>

<?php 
    ini_set('display_errors', '1'); 
    include 'connection.php';
?>

<!DOCTYPE html>
<html lang="en">
    <head>
        
        <script src="./index.js"></script>

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
                    <a href="#" id="runpy">
                        <span class="material-icons-round">refresh</span>
                        <h3>Refresh</h3>
                    </a>

                    <a href="#">
                        <span class="material-icons-round">logout</span>
                        <h3>Logout</h3>
                    </a>

                </div>

            </aside>
            <!-------------------------------------- END OF ASIDE ------------------------------------->
            <main>
                <div class="recent-comments tables">
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
                            <?php
                                
                                $query = "SELECT * FROM tellows";
                                #$insert_query = "INSERT INTO num VALUES ('345')";
                                $result = mysqli_query($conn, $query);

                                $resultCheck =  mysqli_num_rows($result);
                                #$res = mysqli_fetch_array($result);
                                
                                    $i = 0;
                                    while($rows = mysqli_fetch_assoc($result) and $i <= 100){
                                        $i++;
                            ?>
                                        <tr>
                                            <td><?php echo $rows['Number']; ?></td>
                                            <td><?php echo $rows['Comment']; ?></td>
                                            <td><?php echo $rows['Type']; ?></td>
                                            <td><?php echo $rows['Score']; ?></td>
                                        </tr>
                                <?php
                                    }
                                ?>
                        </tbody>
                    </table>
                </div>
                <div class="recents-updates tables">
                <h1>Indicators of compromises</h1>
                <div class="updates">
                    <div class="update">
                        
                    </div>
                </div>
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
            
        </div>

        

    </body>

</html>
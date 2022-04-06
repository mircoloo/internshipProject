<?php
ini_set('display_errors', '1');
include 'connection.php';
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
    <link rel="stylesheet" href="style.css">
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

                <a href="./stats.php">
                    <span class="material-icons-round">query_stats</span>
                    <h3>Analytics</h3>
                </a>
                <a href="#" id="runpy">
                    <span class="material-icons-round">refresh</span>
                    <h3>Refresh</h3>
                </a>

             

            </div>

        </aside>
        <!-------------------------------------- END OF ASIDE ------------------------------------->
        <main>
            <div class="section">
                <h1>Dashboard</h1>
                <div class="teldata-div tables">
                    <h1 class="table-title">Teldata</h1>

                    <table>
                        <thead>
                            <tr>
                                <th class="number-th">Number</th>
                                <th>Comment</th>
                                <th>Type</th>
                                <th>Researchs</th>
                                <th>Score</th>
                                <th>Source</th>
                            </tr>
                        </thead>
                        <tbody>
                            <?php
                            //show databse rows 
                            $query = "SELECT * FROM teldata";
                            $result = mysqli_query($conn, $query);
                            $resultCheck =  mysqli_num_rows($result);
                            $i = 0;
                            while ($rows = mysqli_fetch_assoc($result) and $i < 5) {
                                $i++;
                            ?>
                                <tr>
                                    <td><?php echo $rows['number']; ?></td>
                                    <td><?php echo $rows['comment']; ?></td>
                                    <td><?php echo $rows['type']; ?></td>
                                    <td><?php if($rows['researchs'] != -1){echo $rows['researchs'];}
                                                else{echo "--";}; ?></td>
                                    <td><?php echo $rows['score']; ?></td>
                                    <td><?php echo $rows['source']; ?></td>
                                </tr>
                            <?php
                            }
                            ?>
                        </tbody>
                    </table>
                </div>
                <!-- #endregion telData -->
                <!-- #region twitter cards-->

                <?php include 'cards.php' ?>

                
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
            <div class="ioc-div">
                <h2>IOC</h2>
                <div class="ioc-table tables">
                    <table>
                        <thead>
                            <tr>
                                <th class="ioc-th">IOC</th>
                                <th>Total</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>Amazon</td>
                                <td>342</td>
                            </tr>
                            <tr>
                                <td>Poste</td>
                                <td>23</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
            <div class="ioc-div">
                <h2>Entities</h2>
                <div class="ioc-table tables">
                    <table>
                        <thead>
                            <tr>
                                <th class="ioc-th">IOC</th>
                                <th>Total</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>Amazon</td>
                                <td>342</td>
                            </tr>
                            <tr>
                                <td>Poste</td>
                                <td>23</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
        <!-- END OF TOP -->

    </div>


    <script src="./index.js"></script>
</body>

</html>
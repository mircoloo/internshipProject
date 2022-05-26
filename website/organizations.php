<?php
include 'DBconnection.php';
?>
<h1 class="table-title" style="text-align: center;">Suspicious Links</h1>
<div class="org-container">



    <table>

        <thead>
            <tr>
                <td id="link-top-header">
                    <div>Links</div>
                    <div id="links-num"><?php 
                        $query = "SELECT COUNT(link) FROM twittdata WHERE CHAR_LENGTH(link)>0";
                        $result = mysqli_query($conn, $query);
                        $resultCheck =  mysqli_fetch_array($result);
                        echo $resultCheck[0];    
                    ?></div>
                </td>
                
            </tr>
        </thead>
        <tbody>
            <?php 
                //$query = "SELECT * from twittdata WHERE CHAR_LENGTH(link)>0 LIMIT 3";
                $query = "SELECT link, COUNT(*) AS n
                                FROM twittdata
                                GROUP BY link
                                HAVING CHAR_LENGTH(link)>0;";
                $result = mysqli_query($conn, $query);
                //$result2 = mysqli_query($conn, $query2);
                $resultCheck =  mysqli_num_rows($result);
                while($rows = mysqli_fetch_assoc($result)){
                    ?>
                    <tr><td><?php echo$rows['link'] ?></td><td><?php echo$rows['n'] ?></td></tr>
                    <?php 
                }
                ?>
                
        </tbody>
    </table>

</div>
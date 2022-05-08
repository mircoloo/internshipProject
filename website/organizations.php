<?php
include 'DBconnection.php';
?>
<h1 class="table-title" style="text-align: center;">Links</h1>
<div class="org-container">



    <table>

        <thead>
            <tr>
                <td id="link-top-header">
                    <div>Suspicious Links</div>
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
                $query = "SELECT * from twittdata WHERE CHAR_LENGTH(link)>0 LIMIT 3";
                $result = mysqli_query($conn, $query);
                $resultCheck =  mysqli_num_rows($result);
                while($rows = mysqli_fetch_assoc($result)){
                    ?>
                    <tr><td><?php echo$rows['link'] ?></td></tr>
                    <?php 
                }
                ?>
                
        </tbody>
    </table>

</div>
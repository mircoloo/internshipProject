<?php require 'connection.php'; 
        require 'config.php';
?>
<h1 class="table-title">Twitter</h1>
<div class="cards">

    <?php
    //show databse rows 
    $query = "SELECT DISTINCT * FROM twittdata ORDER BY ID DESC LIMIT " . $GLOBALS['CARDS_TO_DISPLAY'];
    $result = mysqli_query($conn, $query);
    $resultCheck =  mysqli_num_rows($result);
    while ($rows = mysqli_fetch_assoc($result)) {
    ?>
        <div class="card" onclick="clickcard">
            <div class="creation-date"><?php echo $rows['creation']; ?></div>
            <div><?php echo $rows['comment']; ?></div>
            <div class="nickname"><a href="<?php echo  "https://twitter.com/MarkTabNet/status/" . $rows['ID'] ?>" target="_blank"><?php echo $rows['nickname']; ?></a></div>  
            <a href="<?php echo $rows['imageurl'] ?>" target="_blank"><div class="image"><img src="<?php echo $rows['imageurl'] ?>" alt=""></div></a> 
        </div>

    <?php
    }
    ?>

</div>
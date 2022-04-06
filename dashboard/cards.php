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
    $i = 0;
    while ($rows = mysqli_fetch_assoc($result) and $i < 3) {
        $i++;
    ?>
        <div class="card">
            <div class="creation-date"><?php echo $rows['creation']; ?></div>
            <div><?php echo $rows['comment']; ?></div>
            <div class="nickname"><a href="<?php echo  "https://twitter.com/MarkTabNet/status/" . $rows['ID'] ?>"><?php echo $rows['nickname']; ?></a></div>  
            <div class="image"><img src="<?php echo $rows['imageurl'] ?>" alt=""></div>
        </div>

    <?php
    }
    ?>

</div>
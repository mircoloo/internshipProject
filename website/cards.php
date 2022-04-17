<?php 
    require 'DBconnection.php'; 
?>
<!-- Cards of twitter datas -->
<div class="swiper mySwiper">
<h1 class="table-title">Twitter</h1>
    <div class="swiper-wrapper cardBox">
        <?php
        //show databse rows 
        $query = "SELECT DISTINCT * FROM twittdata ORDER BY ID DESC LIMIT " . $GLOBALS['CARDS_TO_DISPLAY'];
        $result = mysqli_query($conn, $query);
        $resultCheck =  mysqli_num_rows($result);
        while ($rows = mysqli_fetch_assoc($result)) {
        ?>
            <div class="swiper-slide card">
                <div class="creation-date"><?php echo $rows['creation']; ?></div>
                <div class="comment"><?php echo $rows['comment']; ?></div>
                <div class="nickname"><a href="<?php echo  "https://twitter.com/MarkTabNet/status/" . $rows['ID'] ?>" target="_blank"><?php echo $rows['nickname']; ?></a></div>  
                <a href="<?php echo $rows['imageurl'] ?>" target="_blank">
                    <div class="image"><img src="<?php echo $rows['imageurl'] ?>" alt=""></div>
                </a> 
            </div>

        <?php
        }
        ?>

    </div>
    <!-- <div class="swiper-button-next"></div>
    <div class="swiper-button-prev"></div> -->
    <div class="swiper-pagination"></div>
</div>
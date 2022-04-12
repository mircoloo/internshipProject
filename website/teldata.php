<div class="teldata-div">
    <h1 class="table-title">Teldata</h1>
    <!-- teldata table -->
    <table class="teldata-table">

        <!-- form to filter results -->
        <div class="selector">
            <!-- posto form --> 
            <form action="#" method="POST">
                <!-- options -->
                <select class="select" name="choice">
                    <optgroup label="Seleziona filtro">
                        <option value="all">All</option>
                        <option value="truffa">Truffa</option>
                        <option value="numero serio">Numero serio</option>
                        <option value="sconosciuto (1)">Sconosciuto</option>
                    </optgroup>
                    <optgroup label="Per Score">
                        <option value="score-slider">Score slider</option>
                    </optgroup>
                </select>
                <!-- submit button -->
                <input class="submit" type="submit" value="SELECT">
                <?php 
                    require 'queryConfig.php';     
                ?>
            </form>
        </div>

        <thead>
            <th class="number-th">Number</th>
            <th>Comment</th>
            <th>Type</th>
            <th>Researchs</th>
            <th>Score</th>
            <th>Source</th>
        </thead>
        <tbody>
            <?php


            $resultCheck =  mysqli_num_rows($result);
            $query = $GLOBALS['QUERY'];
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
                </tr>
            <?php
            }
            ?>
        </tbody>
    </table>


</div>

</div>
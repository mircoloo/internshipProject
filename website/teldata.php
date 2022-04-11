
<div class="teldata-div">
    <h1 class="table-title">Teldata</h1>

    <table class="teldata-table">
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
            //show databse rows 
            $query = $GLOBALS['QUERY'];  
            $result = mysqli_query($conn, $query);
            $resultCheck =  mysqli_num_rows($result);
            $i = 0;
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

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
                <th>Organization</th>
            </tr>
        </thead>
        <tbody>
            <?php
            //show databse rows 
            $query = "SELECT * FROM teldata ORDER BY comment DESC LIMIT " . $GLOBALS['TELDATA_TO_DISPLAY'];
            $result = mysqli_query($conn, $query);
            $resultCheck =  mysqli_num_rows($result);
            while ($rows = mysqli_fetch_assoc($result)) {
            ?>
                <tr>
                    <td><?php echo $rows['number']; ?></td>
                    <td><?php echo $rows['comment']; ?></td>
                    <td><?php echo $rows['type']; ?></td>
                    <td><?php if ($rows['researchs'] != -1) {
                            echo $rows['researchs'];
                        } else {
                            echo "--";
                        }; ?></td>
                    <td><?php echo $rows['score']; ?></td>
                    <td><?php echo $rows['source']; ?></td>
                    <td><?php echo $rows['organization']; ?></td>
                </tr>
            <?php
            }
            ?>

        </tbody>
    </table>
    <form id="search-form" action="search_num.php" method="POST">
        <input type="text" placeholder="Number" name="number">
        <input type="submit" value="Search">
    </form>
</div>
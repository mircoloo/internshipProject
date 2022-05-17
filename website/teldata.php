<div class="teldata-div">
    <h1 class="table-title">Teldata</h1>
    <!-- form to filter results -->
    <div class="selector">
        <!-- posto form -->
        <form class="form" action="#" method="POST">
            <!-- options -->
            <select class="select" name="choice">
                <optgroup label="Seleziona filtro">
                    <option value="all">All</option>
                    <option value="truffa">Truffa</option>
                    <option value="numero serio">Numero serio</option>
                    <option value="sconosciuto">Sconosciuto</option>
                    <option value="telemarketing">Telemarketing</option>
                </optgroup>
                <optgroup label="Per Score">
                    <option value="score-slider">Score slider</option>
                </optgroup>
            </select>
            <?php
            ?>
            <input id="score-slider" type="range" min="1" max="10">
            <span id="show-score-value"></span>
        </form>
        
    </div>
    <!-- teldata table -->
    <table class="teldata-table">
        <thead>
            <th class="number-th">Number</th>
            <th>Comment</th>
            <th>Type</th>
            <th>Researchs</th>
            <th>Score</th>
            <th>Source</th>
            <th>Organization</th>
        </thead>
        <tbody class="teldata-table-tbody">
        </tbody>
    </table>
    <div class="show-buttons">
        <button class="show-more-btn"> SHOW MORE </button>
        <button class="show-less-btn"> SHOW LESS </button>
    </div>
    

</div>


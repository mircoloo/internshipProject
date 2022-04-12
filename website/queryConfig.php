
<?php
$choice = filter_input(INPUT_POST, "choice");

            switch($choice){

                case 'all':
                        $GLOBALS['QUERY'] = "select * from teldata"; break;
                case 'score-slider':  ?> 
            
                    <input type='range'  name='score-range' min= '1' max='10' id='slider'> 
                    <span id="slider_value">-</span> <?php break;  

                default: $GLOBALS['QUERY'] = "select * from teldata where Type = '" . $choice . "'";
                    break;
            }

           
?>
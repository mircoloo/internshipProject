

//menù toggle

let toggle = document.querySelector('.toggle');
let left = document.querySelector('.left');
let main = document.querySelector('.main');
let table = $(".teldata-table")


toggle.onclick = function(){
    left.classList.toggle('active');
    main.classList.toggle('active');
}




$(document).ready(function(){
    var commentCount = 0;
    $(".show-more-btn").click(function(){
        commentCount += 4;
        $.ajax({
            method: 'POST',
            url: "website/load-data.php",
            data: {"commentCount": commentCount},
            success: function(resultData) {  
                $(".teldata-table-tbody").html(resultData);
            
             }
      });

    });
    $(".show-less-btn").click(function(){
        if(commentCount >= 4){commentCount -= 4
        $.ajax({
            method: 'POST',
            url: "website/load-data.php",
            data: {"commentCount": commentCount},
            success: function(resultData) {  
                $(".teldata-table-tbody").html(resultData);
            
             }
      });
        }
    });

    

    $('select').on('change', function() {
        $select = $('.select[name=choice] option').filter(':selected').val();
        $.ajax({
            method: 'POST',
            url: "website/load-data.php",
            data: {"query": $select},
            success: function(resultData) {  
                if($select != 'score-slider'){
                    $("#score-slider").hide();
                    $("#show-score-value").hide();
                }else{
                    $("#score-slider").show();
                    $("#show-score-value").show();
                }  
                if($select != 'all'){
                    $(".show-buttons").hide();
                }else{
                    $(".show-buttons").show();
                }
                $(".teldata-table-tbody").html(resultData);
                
        }
      });
    });      


    // ================ SCORE SLIDER CODE =========================
    $('#score-slider').on('change', function() {
        $score = $(this).val()
        $.ajax({
            method: 'POST',
            url: "website/load-data.php",
            data: {"score": $score},
            success: function(resultData) {
                $(".teldata-table-tbody").html(resultData);
                $("#show-score-value").text($score); 
                if($score <= 4){
                    $('#score-slider').css('accent-color', 'green');
                }else if($score >= 5 && $score <=7){
                    $('#score-slider').css('accent-color', 'yellow');
                }else{
                    $('#score-slider').css('accent-color', 'red');
                }   

                
            }
        });
    });

    //take slider value and display it
$(document).on('input', '#slider', function() {
    $('#slider_value').html( $(this).val() );
});

});






 



//menù toggle

let toggle = document.querySelector('.toggle');
let left = document.querySelector('.left');
let main = document.querySelector('.main');
let table = $(".teldata-table")


toggle.onclick = function(){
    left.classList.toggle('active');
    main.classList.toggle('active');
}

//take slider value and display it
$(document).on('input', '#slider', function() {
    $('#slider_value').html( $(this).val() );
});








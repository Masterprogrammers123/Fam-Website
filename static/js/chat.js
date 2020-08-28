console.warn("[APP] App is on.")

function send() {
    console.log("Sent.")
}
function ready() {
    console.log('Ready');
}

$(function() {
    $('a#button-addon2').bind('click', function() {
        $.getJSON('stuff',
            function(data) {
            //do nothing
        });
    return false;
    });
});



function checkForm() {}
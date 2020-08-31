
console.warn("[APP] App is on.")

$(function() {
    $('button#button-addon2').bind('click', function() {
            $.getJSON('/handle_sockets',
                function(data) {
                //do nothing
            });
        return false;
        });
});
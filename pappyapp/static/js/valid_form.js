$(document).ready(function(){

    var $query = $('#query_text_form');
        $reset = $('query_reset');
        
        /**
        this function is called when the entered key is pressed while entering 
        the address in the form textarea
        **/
    $query.on('keydown', function(e){

        if(e.keyCode == 13){
            e.preventDefault();
            /**
            test if an adress had been writen
            **/
            if ($query.val() == "") {
                alert("N'oublies pas de me poser une question avant de cliquer !")
                return 0;
            }

            /**
            hide btn reset and show spinner
            **/
            $('#query_reset').hide();
            $('#spinner').show();
            
            /**
            send query to the web server and receive response from the server
            **/ 
            $.post( "/question", { query_text_form: $query.val() })
              .done(function( data ) {
                $('#response').html(data['response']);
                $('#otherplaces').html(data['otherplaces']);
                initMap(data['lat'], data['lng']);
                $('#map').show();
                $('#spinner').hide();
                $('#query_reset').show();
            });
        };
    });

    /**
    this function is called when we click on the reset button 
    in the form textarea
    **/
    $reset.on('click', function(e){
        e.preventDefault();
        $('#response').html("");
        $('#map').hide();
        $('#otherplaces').html(""); 
    });
});
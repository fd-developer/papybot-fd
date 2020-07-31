$(document).ready(function(){

    var $query = $('#query_text_form');
        $reset = $('query_reset');

    $query.on('keydown', function(e){

        if(e.keyCode == 13){
            e.preventDefault();

            if ($query.val() == "") {
                alert("N'oublies pas de me poser une question avant de cliquer !")
                return 0;
            }

            $('#query_reset').hide();
            $('#spinner').show();
            
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

    $reset.on('click', function(e){
        e.preventDefault();
        $('#response').html("");
        $('#map').hide();
        $('#otherplaces').html(""); 
    });
});
$(document).ready(function(){

    var $query = $('#query_text_form'),
        $envoi = $('#query-envoi');
        $reset = $('query-reset');

    $envoi.on('click', function(e){
        e.preventDefault();

        if ($query.val() == "") {
            alert("N'oublies pas de me poser une question avant de cliquer !")
            return 0;
        }

        $.post( "/question", { query_text_form: $query.val() })
          .done(function( data ) {
            $('#response').html(data['response']);
            $('#otherplaces').html(data['otherplaces']);
            initMap(data['lat'], data['lng']);
            $('#map').show();
        });

    });

    $reset.on('click', function(e){
        e.preventDefault();
        $('#response').html("");
        $('#map').hide();
        $('#otherplaces').html("");
    });
});

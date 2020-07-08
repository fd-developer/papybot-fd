$(document).ready(function(){

    var $query = $('#query_text_form'),
        $envoi = $('#query-envoi');
        $reset = $('query-reset');

    $envoi.on('click', function(e){
        e.preventDefault(); // on annule la fonction par défaut du bouton d'envoi

        if ($query.val() == "") {
            alert("N'oublies pas de me poser une question avant de cliquer !")
            return 0;
        }

        $.post( "/question", { p1: $query.val() })
          .done(function( data ) {
            $('#response').html(data['response']);
            $('#map').show();
        });

    });

    $reset.on('click', function(e){
        e.preventDefault(); // on annule la fonction par défaut du bouton d'envoi
        
        $('#response').html("");
        $('#map').HIDE();
        
    });
});

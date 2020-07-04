let form = document.getElementById('form-query');

form.addEventListener('submit', function (event) {
    event.preventDefault();

    myFormData = new FormData(form);
    if (myFormData.get('query-text-form') == "") {
        console.log("aucune question")
        return 0;
    }

    fetch("/question",
        {
            method: "POST",
            body: myFormData
        })
        
        .then(response => { return response.json() })
        .then(responseJson => {
            console.log("on passe ici 1")
            console.log(responseJson)
            document.getElementById("lieu").innerHTML = responseJson['adress'] + '<br>';
            document.getElementById("response").innerHTML = responseJson['response']['lat'] + '<br>';
            console.log("on passe ici 2")
        })

});


var map = null;

// Fonction d'initialisation de la carte
// code repris sur :
// https://nouvelle-techno.fr/actualites/pas-a-pas-inserer-une-carte-google-maps-avec-lapi-google-maps-javascript

function initMap(lat,lng) {
	// Créer l'objet "map" et l'insèrer dans l'élément HTML qui a l'ID "map"
	var LatLng = new google.maps.LatLng(lat,lng)
	map = new google.maps.Map(document.getElementById("map"), {
		center: LatLng, 
		zoom: 11, 
		mapTypeId: google.maps.MapTypeId.ROADMAP, 
		// ROADMAP : affiche le plan classique, sans image satellite ni relief ;
		// SATELLITE : pour les photos satellite ;
		// HYBRID : pour afficher les photos satellite avec le plan superposé (les routes, le nom des villes) ;
		// TERRAIN : affiche les différences de reliefs (montagnes, rivières, etc.).
		mapTypeControl: true,
		scrollwheel: false, 
		mapTypeControlOptions: {
			style: google.maps.MapTypeControlStyle.HORIZONTAL_BAR 
		},
		navigationControl: true, 
		navigationControlOptions: {
			style: google.maps.NavigationControlStyle.ZOOM_PAN 
		}
	});

	var marker = new google.maps.Marker({
		position: LatLng,
		map: map
	});
}

window.onload = function(){
	initMap(0,0); 
};

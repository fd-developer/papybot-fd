var map = null;

// map init function
// code found on :
// https://nouvelle-techno.fr/actualites/pas-a-pas-inserer-une-carte-google-maps-avec
// -lapi-google-maps-javascript

function initMap(lat,lng) {
	// create "map" object and insert it in HTML with ID = "map"
	var LatLng = new google.maps.LatLng(lat,lng)
	map = new google.maps.Map(document.getElementById("map"), {
		center: LatLng, 
		zoom: 11, 
		mapTypeId: google.maps.MapTypeId.ROADMAP, 
		// ROADMAP : show classic map
		// SATELLITE : for satellite photos ;
		// HYBRID : to display satellite photos with the superimposed map (roads, names of cities) ;
		// TERRAIN : displays the differences in relief (mountains, rivers, etc.).
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

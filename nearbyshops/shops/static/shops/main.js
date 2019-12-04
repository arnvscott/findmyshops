function setInfoWindow(map, pos, msg){

    // create an info message at a given location
    infoWindow = new google.maps.InfoWindow;

    infoWindow.setPosition(pos);
    infoWindow.setContent(msg);
    infoWindow.open(map);
    map.setCenter(pos);

}

function setLatLngFormFields(lat, lng){

    // record latitude and longitude in the hidden form fields
    document.getElementById("cur_lat").value = lat;
    document.getElementById("cur_lng").value = lng;

}

function markLocations(map, locations){

    var markers = locations.map(function(location){
        pos = {
            lat:location.lat,
            lng:location.lng
        };
        return new google.maps.Marker({position:pos, map: map, label:location.name });
    });

}
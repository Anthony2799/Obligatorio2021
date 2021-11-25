
var strArray = [];

var draggablePolygon; function InitMap() {
    var location = new google.maps.LatLng(-1.2785691284426366, 36.82319944424295);
    var mapOptions = {
        zoom: 13,
        center: location,
        mapTypeId: google.maps.MapTypeId.RoadMap
    };


    var map = new google.maps.Map(document.getElementById('map-canvas'),
        mapOptions);

    var shapeCoordinates = [

        new google.maps.LatLng(39.86232, -4.0694706),
        new google.maps.LatLng(39.86232, -4.0694706)
    ];
    // Construct the polygon
    draggablePolygon = new google.maps.Polygon({
        paths: shapeCoordinates,
        draggable: true,
        editable: true,
        strokeColor: '',
        strokeOpacity: 0.8,
        strokeWeight: 2,
        fillColor: '#ADFF2F',
        fillOpacity: 0.5
    });
    draggablePolygon.setMap(map);
    google.maps.event.addListener(draggablePolygon, "dragend", Getpolygoncoordinates);
    google.maps.event.addListener(draggablePolygon.getPath(), "insert_at", Getpolygoncoordinates);
    google.maps.event.addListener(draggablePolygon.getPath(), "remove_at", Getpolygoncoordinates);
    google.maps.event.addListener(draggablePolygon.getPath(), "set_at", Getpolygoncoordinates);
}

function Getpolygoncoordinates() {
    var len = draggablePolygon.getPath().getLength();
    strArray = [];
    for (var i = 0; i < len; i++) {
        strArray[strArray.length] = { Latitud: draggablePolygon.getPath().getAt(i).toUrlValue(5).split(",")[0], Longitud: draggablePolygon.getPath().getAt(i).toUrlValue(5).split(",")[1] };
    }

}

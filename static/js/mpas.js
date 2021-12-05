var prueba;
let marker;          //variable del marcador
let coords = {
  lat: -1.285047,
  lng: 36.807381
};    //coordenadas obtenidas con la geolocalización
var map;
let zona1 = [
  { lat: -1.2697381346306198, lng: 36.77579530664062 },
  { lat: -1.2896458877827368, lng: 36.762405719238274 },
  { lat: -1.298570002583987, lng: 36.80326112695312 },
{ lat: -1.2649327918431663, lng: 36.803604449707024 },
{ lat: -1.2697381346306198, lng: 36.77579530664062  },
];
let zona2 = [
  { lat: -1.2649327918431663, lng: 36.803604449707024 },
  { lat: -1.2606422996905813, lng: 36.84222825952148 },
  { lat: -1.3052630680195252, lng: 36.82660707421874 },
  { lat: -1.2649327918431663, lng: 36.803604449707024 },
  { lat: -1.2649327918431663, lng: 36.803604449707024  },
  ];
  let zona3 = [
    { lat: -1.2652760309092232, lng: 36.80394777246093 },
    { lat: -1.3157316730715614, lng: 36.80291780419921 },
    { lat: -1.3260286187922565, lng: 36.79519304223632 },
    { lat: -1.3332364553296105, lng: 36.80926927514648 },
    { lat: -1.3265434649566388, lng: 36.84720643945312 },
    { lat: -1.3054346848481215, lng: 36.82643541284179 },
    ];

  let Zonas = (...Znas)=>{
    let locations=[];
    Znas.forEach(element => {
      for(elemento of element){
        let lat = elemento.lat;
        let lng = elemento.lng;
        let aux ={lat, lng}
        locations.push(aux)
      }
    });
    return locations;
  };
  
  //Funcion principal
initMap = function () {
  coords ;
  setMapa(coords);  //pasamos las coordenadas al metodo para crear el mapa

}

function setMapa(coords) {

  //Se crea una nueva instancia del objeto mapa
    map = new google.maps.Map(document.getElementById('map-canvas'),
    {
      zoom: 13,
      center: new google.maps.LatLng(coords.lat,
        coords.lng)

    });

  //Creamos el marcador en el mapa con sus propiedades
  //para nuestro obetivo tenemos que poner el atributo draggable en true
  //position pondremos las mismas coordenas que obtuvimos en la geolocalización
  markerOne = new google.maps.Marker({
    map: map,
    //pnemos false para que no se pueda mover el marcador
    draggable: false,
    position: new google.maps.LatLng(coords.lat,
      coords.lng),

  });
  marker = new google.maps.Marker({
    map: map,
    draggable: true,
    animation: google.maps.Animation.DROP,
    position: new google.maps.LatLng(-1.286900,
    36.807381),
    
  });
  //agregamos un evento al marcador junto con la funcion callback al igual que el evento dragend que indica 
  //cuando el usuario a soltado el marcador
  marker.addListener('click', toggleBounce);

  marker.addListener('dragend', function (event) {
    //escribimos las coordenadas de la posicion actual del marcador dentro del input #coords
    lat =this.getPosition().lat();
    lng = this.getPosition().lng();
    document.getElementById("lat").value = lat;
    document.getElementById('lng').value = lng;
    
    function dist(){
      let extra = new google.maps.LatLng({
          lat: parseFloat(document.getElementById("lat").value), 
          lng: parseFloat(document.getElementById("lng").value)
      })
      var distanceInMeters = google.maps.geometry.spherical.computeDistanceBetween(
          coords,
          extra
          );
      document.getElementById("distancia").value = (distanceInMeters * 0.001);
    }
    
    dist()
  });

  google.maps.event.addListener(map, 'click', function(event) {
    console.log(google.maps.geometry.poly.containsLocation(event.latLng, zona1));
  });


  
  linea();

}


  
  //callback al hacer clic en el marcador lo que hace es quitar y poner la animacion BOUNCE
function toggleBounce() {
  if (marker.getAnimation() !== null) {
    marker.setAnimation(null);
  } else {
    marker.setAnimation(google.maps.Animation.BOUNCE);
  }
}




let linea = ()=>{ 
  let pts= Zonas(zona1,zona2,zona3);
  new google.maps.Polyline({
  path: pts,
  map: map,
  strokeColor: 'rgb(255, 0, 0)',
  strokeWeight: 2
  });
}
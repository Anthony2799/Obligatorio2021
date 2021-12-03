

      
     var marker;          //variable del marcador
     var coords = {
       lat: -1.285047,
       lng: 36.807381
     };    //coordenadas obtenidas con la geolocalización
     
     //Funcion principal
     initMap = function () {
       coords ;
       setMapa(coords);  //pasamos las coordenadas al metodo para crear el mapa
     
     }
     
     function setMapa(coords) {
     
       //Se crea una nueva instancia del objeto mapa
       var map = new google.maps.Map(document.getElementById('map-canvas'),
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
         
       });
       
     
     }
     
     //callback al hacer clic en el marcador lo que hace es quitar y poner la animacion BOUNCE
     function toggleBounce() {
       if (marker.getAnimation() !== null) {
         marker.setAnimation(null);
       } else {
         marker.setAnimation(google.maps.Animation.BOUNCE);
       }
     }


                var marker;          //variable del marcador
                var coords = {};    //coordenadas obtenidas con la geolocalización

                //Funcion principal
                initMap = function () {
                  coords = {
                    lat: -1.285047,
                    lng: 36.807381
                  };
                  setMapa(coords);  //pasamos las coordenadas al metodo para crear el mapa

                }

                function setMapa(coords) {

                  //Se crea una nueva instancia del objeto mapa
                  var map = new google.maps.Map(document.getElementById('map-canvas'),
                    {
                      zoom: 13,
                      center: new google.maps.LatLng(coords.lat,
                        coords.lng)

                    });

                  //Creamos el marcador en el mapa con sus propiedades
                  //para nuestro obetivo tenemos que poner el atributo draggable en true
                  //position pondremos las mismas coordenas que obtuvimos en la geolocalización
                  marker = new google.maps.Marker({
                    map: map,
                    draggable: true,
                    animation: google.maps.Animation.DROP,
                    position: new google.maps.LatLng(coords.lat,
                      coords.lng),

                  });
                  //agregamos un evento al marcador junto con la funcion callback al igual que el evento dragend que indica 
                  //cuando el usuario a soltado el marcador
                  marker.addListener('click', toggleBounce);

                  marker.addListener('dragend', function (event) {
                    //escribimos las coordenadas de la posicion actual del marcador dentro del input #coords
                    document.getElementById('lat').value = this.getPosition().lat();
                    document.getElementById('lng').value = this.getPosition().lng();
                  });
                }

                //callback al hacer clic en el marcador lo que hace es quitar y poner la animacion BOUNCE
                function toggleBounce() {
                  if (marker.getAnimation() !== null) {
                    marker.setAnimation(null);
                  } else {
                    marker.setAnimation(google.maps.Animation.BOUNCE);
                  }
                }
    
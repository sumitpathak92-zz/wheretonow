function initMap() {
        var map = new google.maps.Map(document.getElementById('map'), {
          center: {lat: -34.397, lng: 150.644},
          zoom: 6
        });
        var infoWindow = new google.maps.InfoWindow({map: map});

        // Try HTML5 geolocation.
        if (navigator.geolocation) {
          navigator.geolocation.getCurrentPosition(function(position) {
            var pos = {
              lat: position.coords.latitude,
              lng: position.coords.longitude
            };
            var tempObject = {
                "type": "Feature",
                "properties": {
                    "name": "Coors Field",
                    "amenity": "Baseball Stadium",
                    "popupContent": "This is where the Rockies play!"
                },
                "geometry": {
                    "type": "Point",
                    "coordinates": [pos['lng'], pos['lat']]
                }
            };
            var myLatlng = new google.maps.LatLng(pos['lat'], pos['lng']);
            var marker = new google.maps.Marker({
                 position: myLatlng,
                 title: 'Hello Haldwani!',
                 map: map,
                 draggable: true
            });
            google.maps.event.addListener(marker, 'mouseover', function() {
                marker.setIcon('/home/sumit/Downloads/Slack Filled-50.png')
            })
            // marker.setMap(map);
        
        //adding json into map here

        map.data.addGeoJson(tempObject);
            infoWindow.setPosition(pos);
            infoWindow.setContent('Location found.');
            map.setCenter(pos);
          }, function() {
            handleLocationError(true, infoWindow, map.getCenter());
          });
        } else {
          // Browser doesn't support Geolocation
          handleLocationError(false, infoWindow, map.getCenter());
        }

         //loading json data into map test
        
      }

function handleLocationError(browserHasGeolocation, infoWindow, pos) {
        infoWindow.setPosition(pos);
        infoWindow.setContent(browserHasGeolocation ?
                              'Error: The Geolocation service failed.' :
                              'Error: Your browser doesn\'t support geolocation.');
      }
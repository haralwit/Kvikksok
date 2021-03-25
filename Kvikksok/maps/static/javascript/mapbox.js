
mapboxgl.accessToken = 'pk.eyJ1IjoibGFmaXNlciIsImEiOiJja2dwcmlhaW8wc3h1Mndtb2VtOXplMWp0In0.Vi0BWSGA2uPlDSbm2tb9zQ';//access token
var map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/lafiser/ckmltml3c4hxe17s650pj4blq',  //mapbox style URL
    center: [10.404, 63.417],
    zoom: 12
 });

 function addDataLayer(){
    map.addSource('kvikkleire',{
        type: 'geojson',
        data: 'static/kvikkleireUtlosningOmr.geojson'
    });
    map.addLayer({
        id: 'fareOmrade',
        type: 'fill',
        source: 'kvikkleire',
        paint: {
        'fill-opacity': ['/',1.0,['get', 'skredRisikoKvikkleireKlasse']],
        'fill-color':'#ff0000',
        },
      });
 }

 map.on("load", () => {
    //addDataLayer();
  });

  var coordinatesGeocoder = function (query) {
    // match anything which looks like a decimal degrees coordinate pair
       var matches = query.match(
          /^[ ]*(?:Lat: )?(-?\d+\.?\d*)[, ]+(?:Lng: )?(-?\d+\.?\d*)[ ]*$/i
       );
       if (!matches) {
          return null;
       }
       
       function coordinateFeature(lng, lat) {
          return {
             center: [lng, lat],
             geometry: {
                type: 'Point',
                coordinates: [lng, lat]
             },
             place_name: 'Lat: ' + lat + ' Lng: ' + lng,
             place_type: ['coordinate'],
             properties: {},
             type: 'Feature'
          };
       }
       
       var coord1 = Number(matches[1]);
       var coord2 = Number(matches[2]);
       var geocodes = [];
       
       if (coord1 < -90 || coord1 > 90) {
       // must be lng, lat
          geocodes.push(coordinateFeature(coord1, coord2));
       }
       
       if (coord2 < -90 || coord2 > 90) {
       // must be lat, lng
          geocodes.push(coordinateFeature(coord2, coord1));
       }
       
       if (geocodes.length === 0) {
       // else could be either lng, lat or lat, lng
          geocodes.push(coordinateFeature(coord1, coord2));
          geocodes.push(coordinateFeature(coord2, coord1));
       }
       
       return geocodes;
    };
    
    map.addControl(
       new MapboxGeocoder({
          accessToken: mapboxgl.accessToken,
          localGeocoder: coordinatesGeocoder,
          zoom: 4,
          placeholder: 'Stedsnavn/Koordinater',
          mapboxgl: mapboxgl
       })
    );

    //NavigationControl
    var nav = new mapboxgl.NavigationControl();
    var addmarker_boolen = false; 
    map.addControl(nav, 'top-left');


    document.getElementById("nyttPunkt").onclick = function() {addMarker()};
    //allows user to add a marker
    function addMarker() {
        addmarker_boolen = true;
        console.log('addmarker is ' + addmarker_boolen)
    }

    
    //MapMouseEvent and marker
    map.on('click', function(e) {
        if (addmarker_boolen == true) {
            var marker = new mapboxgl.Marker({
                    color: '#004fa4',
                    draggable: true
                })
                .setLngLat([e.lngLat.lng, e.lngLat.lat])
                .setPopup(
                    new mapboxgl.Popup({})
                    .setLngLat([e.lngLat.lng, e.lngLat.lat])
                    .setHTML("<h1>Hello World!</h1>").addTo(map))
                .addTo(map);

            addmarker_boolen = false;                
        }
    
    });

    

    document.getElementById("post").onclick = function() {getGeojson_points()};
    function getGeojson_points() {
        map.addSource('postnummer',{
                type: 'geojson',
                data: {
                        "type": "FeatureCollection",
                        "name": "postNummer",
                        //"crs": { "type": "name", "properties": { "name": "urn:ogc:def:crs:OGC:1.3:CRS84" } },
                        "features": [
                            { "type": "Feature", "properties": { "postnummer": 1354, "poststed": "B�RUMS VERK" }, "geometry": { "type": "Point", "coordinates": [ 10.495188707896558, 59.942997421825446 ] } },
                            { "type": "Feature", "properties": { "postnummer": 2092, "poststed": "MINNESUND" }, "geometry": { "type": "Point", "coordinates": [ 11.230517825998556, 60.427781233028846 ] } },
                            { "type": "Feature", "properties": { "postnummer": 3536, "poststed": "NORESUND" }, "geometry": { "type": "Point", "coordinates": [ 9.602099500044879, 60.230940730555595 ] } },
                            { "type": "Feature", "properties": { "postnummer": 274, "poststed": "OSLO" }, "geometry": { "type": "Point", "coordinates": [ 10.692964774885331, 59.924863418008385 ] } }
                            ] 
                        }
        }); 

        map.addLayer({
            id: 'postnummer_senter  ',
            type: 'circle',
            source: 'postnummer',
            'paint': {
            'circle-radius': 6,
            'circle-color': '#B42222'
            },
            'filter': ['==', '$type', 'Point']
        });  
    }



